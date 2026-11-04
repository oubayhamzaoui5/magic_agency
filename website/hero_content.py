"""Persisted hero selection shared by the builder and local image editor."""
from pathlib import Path
from html import escape
import hashlib
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'website' / 'content' / 'hero.json'
DEFAULT = {'lanes': [
    [{'image': 'hero/' + key, 'label': key.upper()} for key in
     ['miro', 'pogo', 'forma', 'tempo', 'bloom']],
    [{'image': 'hero/' + key, 'label': key.upper()} for key in
     ['rive', 'onda', 'kova', 'tera', 'orbit']],
    [{'image': 'hero/' + key, 'label': key.upper()} for key in
     ['luma', 'nori', 'folio', 'vela']],
]}


def library():
    result = []
    for folder in ['hero', 'magic', 'concepts', 'uploads']:
        for path in sorted((ROOT / 'assets' / folder).glob('*-480.webp')):
            stem = path.name.removesuffix('-480.webp')
            with Image.open(path) as image:
                width, height = image.size
            variants = {}
            for size in [480, 900, 1400]:
                variant = path.parent / f'{stem}-{size}.webp'
                if variant.is_file():
                    with Image.open(variant) as image:
                        variants[image.width] = f'/assets/{folder}/{stem}-{size}.webp'
            result.append({'id': folder + '/' + stem,
                           'label': stem.replace('-', ' ').capitalize(),
                           'width': width, 'height': height,
                           'src': f'/assets/{folder}/{stem}-480.webp',
                           'srcset': ', '.join(f'{src} {size}w' for size, src in sorted(variants.items()))})
    return result


def read_content():
    content = json.loads(CONTENT.read_text(encoding='utf-8')) if CONTENT.exists() else json.loads(json.dumps(DEFAULT))
    # Preserve both existing columns when upgrading the original editor selection.
    if len(content.get('lanes', [])) == 2:
        content['lanes'].append(json.loads(json.dumps(DEFAULT['lanes'][2])))
    return content


def revision(content):
    return hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()[:16]


def validate(content):
    if not isinstance(content, dict) or set(content) != {'lanes'}:
        raise ValueError('Format de sélection invalide.')
    lanes = content['lanes']
    if not isinstance(lanes, list) or len(lanes) != 3:
        raise ValueError('Trois colonnes sont nécessaires.')
    known = {item['id'] for item in library()}
    clean = []
    for lane in lanes:
        if not isinstance(lane, list) or not 1 <= len(lane) <= 12:
            raise ValueError('Gardez entre 1 et 12 images par colonne.')
        row = []
        for item in lane:
            if not isinstance(item, dict) or item.get('image') not in known:
                raise ValueError('Choisissez une image de la bibliothèque.')
            label = item.get('label', '')
            if not isinstance(label, str) or len(label) > 80:
                raise ValueError('Le nom est limité à 80 caractères.')
            row.append({'image': item['image'], 'label': label.strip()})
        clean.append(row)
    return {'lanes': clean}


def write_content(content):
    CONTENT.parent.mkdir(exist_ok=True)
    temporary = CONTENT.with_suffix('.tmp')
    temporary.write_text(json.dumps(content, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(CONTENT)


def render_lanes(mobile=False):
    assets = {item['id']: item for item in library()}
    selections = read_content()['lanes']
    if mobile:
        # Same saved imagery and reading order, arranged in two horizontal rows.
        items = [item for lane in selections for item in lane]
        midpoint = (len(items) + 1) // 2
        selections = [items[:midpoint], items[midpoint:]]
    lanes = []
    for index, items in enumerate(selections):
        # Enough repeated artwork to cover tall walls even when a column has one image.
        repeats = max(1, (12 + len(items) - 1) // len(items))
        tiles = []
        for item in items * repeats:
            asset = assets[item['image']]
            picture = (f'<img src="{escape(asset["src"], quote=True)}" '
                       f'srcset="{escape(asset["srcset"], quote=True)}" '
                       'sizes="(min-width:1650px) 244px, (min-width:1280px) 182px, 200px" '
                       f'width="{asset["width"]}" height="{asset["height"]}" '
                       'alt="" loading="eager" decoding="async">')
            ratio = asset['width'] / asset['height']
            tiles.append(f'<div class="wall-tile" style="--art-ratio:{ratio:.7f}">{picture}<span>{escape(item["label"])}</span></div>')
        group = ''.join(tiles)
        duration = len(items) * repeats * (156 / 28 if mobile else 12)
        lanes.append(f'<div class="wall-lane lane-{index}"><div class="wall-track" style="animation-duration:{duration}s">'
                     f'<div class="wall-group">{group}</div>'
                     f'<div class="wall-group wall-copy" aria-hidden="true">{group}</div></div></div>')
    return ''.join(lanes)
