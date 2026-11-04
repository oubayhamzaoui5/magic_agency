"""Build static delivery files without source, credentials, or bitmap masters."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, urljoin, unquote
from hashlib import sha256
import argparse
import json
import os
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
DELIVERY = {'.webp', '.svg', '.avif', '.css', '.js', '.woff', '.woff2', '.jpg', '.jpeg'}


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('src', 'href'):
            if attrs.get(key):
                self.urls.add(attrs[key])
        if attrs.get('srcset'):
            self.urls.update(item.strip().split()[0] for item in attrs['srcset'].split(','))


def build(output, live_links=False):
    output = Path(output).resolve()
    if output == ROOT or ROOT.is_relative_to(output) or (output.exists() and any(output.iterdir())):
        raise ValueError('Choose an empty output directory, separate from the source root.')
    output.mkdir(parents=True, exist_ok=True)
    files = {ROOT/'index.html', ROOT/'robots.txt', ROOT/'sitemap.xml', ROOT/'magiclogo.png', ROOT/'logo.png', ROOT/'nav.png'}
    pages = [ROOT/'index.html', *sorted((ROOT/'directions').glob('*/index.html'))]
    files.update(pages)
    files.update((ROOT/'assets/fonts').glob('*-OFL.txt'))
    files.update(p for p in (ROOT/'assets').rglob('*') if p.is_file() and p.suffix.lower() in DELIVERY)
    references = set()
    for page in pages:
        parser = References()
        parser.feed(page.read_text(encoding='utf-8'))
        references.update((page, url) for url in parser.urls)
    for css in (ROOT/'assets').rglob('*.css'):
        references.update((css, url) for url in re.findall(r'url\([\"\']?([^\)\"\']+)', css.read_text(encoding='utf-8')))
    for source, url in references:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path or parts.path.startswith('/admin'):
            continue
        relative = urlsplit(urljoin('/'+source.relative_to(ROOT).as_posix(), url)).path
        target = (ROOT/unquote(relative).lstrip('/')).resolve()
        if not target.is_relative_to(ROOT):
            raise ValueError('Reference leaves source root: '+relative)
        if target.is_dir():
            target = target/'index.html'
        if not target.is_file():
            raise FileNotFoundError(relative)
        files.add(target)
    if live_links:
        entries = {source.relative_to(ROOT).parts[0] for source in files}
        allowed = {'index.html', 'assets', 'directions', 'robots.txt', 'sitemap.xml', 'magiclogo.png', 'logo.png', 'nav.png'}
        if not entries.issubset(allowed):
            raise ValueError('Live delivery must contain only the approved static entry points.')
        for name in sorted(entries):
            (output/name).symlink_to(os.path.relpath(ROOT/name, output), target_is_directory=(ROOT/name).is_dir())
    manifest = []
    for source in sorted(files):
        relative = source.relative_to(ROOT)
        target = output/relative
        if not live_links:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
        manifest.append({'path': relative.as_posix(), 'bytes': target.stat().st_size, 'sha256': sha256(target.read_bytes()).hexdigest()})
    return manifest


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--live-links', action='store_true', help='Linux server: link approved static entry points in a clean Git checkout so pulls update the live files.')
    args = parser.parse_args()
    manifest = build(args.output, live_links=args.live_links)
    Path(args.manifest).write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f'Built {len(manifest)} public files, {sum(item["bytes"] for item in manifest)} bytes.')
