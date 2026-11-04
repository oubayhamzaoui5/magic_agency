"""Loopback-only Magic preview and password-protected image editor."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from pathlib import Path
from urllib.parse import urlsplit, unquote
from io import BytesIO
import hashlib
import hmac
import json
import os
import secrets
import threading
import time
import warnings

from PIL import Image, ImageOps, UnidentifiedImageError
from hero_content import ROOT, CONTENT, read_content, write_content, validate, revision, library
from build_magic import build

AUTH_FILE = Path(os.environ.get('LOCALAPPDATA', Path.home())) / 'Magic360' / 'admin-auth.json'
SESSIONS = {}
ATTEMPTS = {}
LOCK = threading.RLock()
ORIGINS = {'http://127.0.0.1:8000', 'http://localhost:8000'}
MAX_UPLOAD = 10 * 1024 * 1024
Image.MAX_IMAGE_PIXELS = 24_000_000


class PreviewHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, max-age=0')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

    def safe_host(self):
        if self.headers.get('Host') not in {'127.0.0.1:8000', 'localhost:8000'}:
            self.reply(403, {'error': 'Accès local uniquement.'})
            return False
        return True

    def reply(self, code, value, cookie=None):
        raw = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(raw)))
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()
        self.wfile.write(raw)

    def session(self):
        try:
            cookie = SimpleCookie(self.headers.get('Cookie', ''))
            token = cookie['magic_admin'].value if 'magic_admin' in cookie else ''
        except Exception:
            return None
        with LOCK:
            session = SESSIONS.get(token)
            if session and session['expires'] > time.time():
                return session
            SESSIONS.pop(token, None)
        return None

    def require_session(self):
        session = self.session()
        if not session:
            self.reply(401, {'error': 'Connectez-vous pour modifier les images.'})
        return session

    def do_HEAD(self):
        self.do_GET(head=True)

    def do_GET(self, head=False):
        if not self.safe_host():
            return
        path = unquote(urlsplit(self.path).path)
        if path == '/api/admin/state':
            session = self.require_session()
            if session:
                content = read_content()
                self.reply(200, {'content': content, 'revision': revision(content),
                                 'library': library(), 'csrf': session['csrf']})
            return
        if path in {'/admin', '/admin/'}:
            self.send_file(ROOT / 'website' / 'admin' / 'index.html', head)
            return
        if path in {'/admin/editor.css', '/admin/editor.js'}:
            self.send_file(ROOT / 'website' / 'admin' / path.rsplit('/', 1)[1], head)
            return
        # Never expose server source, stored content, credentials or repository internals.
        parts = Path(path).parts
        if any(part.startswith('.') for part in parts) or '\\' in path:
            self.send_error(404)
            return
        permitted = path in {'/', '/index.html', '/robots.txt', '/sitemap.xml', '/magiclogo.png', '/website/icon-preview.html'}
        permitted = permitted or (path.startswith('/assets/') and Path(path).suffix.lower() in
                                 {'.webp', '.png', '.jpg', '.jpeg', '.svg', '.css', '.js', '.woff2', '.woff'})
        permitted = permitted or (path.startswith('/directions/') and (path.endswith('/') or path.endswith('/index.html')))
        target = Path(self.translate_path(path)).resolve()
        if not permitted or not target.is_relative_to(ROOT):
            self.send_error(404)
            return
        if head:
            super().do_HEAD()
        else:
            super().do_GET()

    def send_file(self, path, head=False):
        raw = path.read_bytes()
        self.send_response(200)
        mime = {'.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
                '.js': 'application/javascript; charset=utf-8'}[path.suffix]
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(raw)))
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' blob:; font-src 'self'; connect-src 'self'; frame-ancestors 'self'; base-uri 'none'; form-action 'self'")
        self.end_headers()
        if not head:
            self.wfile.write(raw)

    def read_body(self, limit):
        try:
            size = int(self.headers.get('Content-Length', '0'))
        except ValueError:
            raise ValueError('Taille du fichier invalide.')
        if not 0 < size <= limit:
            raise ValueError('Fichier trop volumineux (10 Mo maximum) ou vide.')
        return self.rfile.read(size)

    def do_POST(self):
        if not self.safe_host():
            return
        if self.headers.get('Origin') not in ORIGINS:
            self.reply(403, {'error': 'Rechargez cet éditeur depuis le site local.'})
            return
        path = urlsplit(self.path).path
        try:
            if path == '/api/login':
                self.login()
                return
            session = self.require_session()
            if not session:
                return
            if not hmac.compare_digest(self.headers.get('X-CSRF-Token', ''), session['csrf']):
                self.reply(403, {'error': 'Session invalide. Rechargez la page.'})
                return
            if path == '/api/logout':
                with LOCK:
                    for token, current in list(SESSIONS.items()):
                        if current is session:
                            SESSIONS.pop(token)
                self.reply(200, {'ok': True}, 'magic_admin=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0')
            elif path == '/api/admin/upload':
                self.upload()
            elif path == '/api/admin/hero':
                data = json.loads(self.read_body(64000))
                with LOCK:
                    previous = read_content()
                    if data.get('revision') != revision(previous):
                        self.reply(409, {'error': 'Les images ont changé ailleurs. Rechargez avant de continuer.'})
                        return
                    content = validate(data.get('content'))
                    write_content(content)
                    try:
                        build()
                    except Exception:
                        write_content(previous)
                        raise
                self.reply(200, {'ok': True, 'revision': revision(content)})
            else:
                self.reply(404, {'error': 'Adresse inconnue.'})
        except (ValueError, TypeError, KeyError, json.JSONDecodeError):
            self.reply(400, {'error': 'Sélection invalide. Vérifiez les images et réessayez.'})
        except Exception:
            self.reply(500, {'error': 'Enregistrement impossible. Vos changements restent dans cet éditeur ; réessayez.'})

    def login(self):
        data = json.loads(self.read_body(2000))
        password = data.get('password', '')
        if not isinstance(password, str) or len(password) > 256:
            self.reply(400, {'error': 'Mot de passe invalide.'})
            return
        now = time.time()
        ip = self.client_address[0]
        with LOCK:
            tries = [value for value in ATTEMPTS.get(ip, []) if now - value < 60]
            ATTEMPTS[ip] = tries
            if len(tries) >= 5:
                self.reply(429, {'error': 'Trop de tentatives. Réessayez dans une minute.'})
                return
            record = json.loads(AUTH_FILE.read_text(encoding='utf-8'))
            candidate = hashlib.pbkdf2_hmac('sha256', password.encode(), bytes.fromhex(record['salt']), 310000).hex()
            if not hmac.compare_digest(candidate, record['hash']):
                tries.append(now)
                self.reply(401, {'error': 'Mot de passe incorrect.'})
                return
            ATTEMPTS.pop(ip, None)
            for key, value in list(SESSIONS.items()):
                if value['expires'] <= now:
                    SESSIONS.pop(key)
            token = secrets.token_urlsafe(32)
            SESSIONS[token] = {'csrf': secrets.token_urlsafe(32), 'expires': now + 8 * 3600}
        self.reply(200, {'ok': True}, f'magic_admin={token}; HttpOnly; SameSite=Strict; Path=/; Max-Age=28800')

    def upload(self):
        raw = self.read_body(MAX_UPLOAD)
        try:
            with warnings.catch_warnings():
                warnings.simplefilter('error', Image.DecompressionBombWarning)
                image = Image.open(BytesIO(raw))
                if image.format not in {'JPEG', 'PNG', 'WEBP'}:
                    raise ValueError()
                image.load()
                image = ImageOps.exif_transpose(image)
                if image.width < 100 or image.height < 100 or image.width * image.height > 24_000_000:
                    raise ValueError()
                image = image.convert('RGBA' if 'A' in image.getbands() else 'RGB')
        except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombWarning, Image.DecompressionBombError):
            self.reply(400, {'error': 'Choisissez un JPG, PNG ou WebP valide, de 100 px minimum et 24 mégapixels maximum.'})
            return
        stem = 'image-' + secrets.token_hex(8)
        folder = ROOT / 'assets' / 'uploads'
        folder.mkdir(exist_ok=True)
        created = []
        try:
            for width in [480, 900, 1400]:
                scale = min(width / image.width, 4096 / image.height)
                size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
                resized = image.resize(size, Image.Resampling.LANCZOS)
                target = folder / f'{stem}-{width}.webp'
                resized.save(target, 'WEBP', quality=88)
                created.append(target)
        except Exception:
            for target in created:
                target.unlink(missing_ok=True)
            raise
        self.reply(200, {'image': next(item for item in library() if item['id'] == 'uploads/' + stem)})


if __name__ == '__main__':
    if not AUTH_FILE.exists():
        raise SystemExit('Local administrator credential is missing.')
    if not CONTENT.exists():
        write_content(read_content())
    handler = partial(PreviewHandler, directory=str(ROOT))
    ThreadingHTTPServer(('127.0.0.1', 8000), handler).serve_forever()
