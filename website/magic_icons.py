"""Magic's original SVG icon family. Source of truth for sprite and editable icons."""
from pathlib import Path

# Curved four-point sparks echo the original wizard's wand; forms remain functional.
SPARK='M16 3C17.2 11.3 20.7 14.8 29 16C20.7 17.2 17.2 20.7 16 29C14.8 20.7 11.3 17.2 3 16C11.3 14.8 14.8 11.3 16 3Z'
SMALL='M25 3C25.4 6.1 26.9 7.6 30 8C26.9 8.4 25.4 9.9 25 13C24.6 9.9 23.1 8.4 20 8C23.1 7.6 24.6 6.1 25 3Z'
ACCENT='fill="var(--icon-accent,#ead28c)" stroke="none"'
ICONS={
 'whatsapp':'<g transform="scale(1.333333)" fill="currentColor" stroke="none"><path d="M20.52 3.48A11.91 11.91 0 0 0 12.05 0C5.47 0 .11 5.35.1 11.94c0 2.1.55 4.15 1.6 5.96L0 24l6.26-1.64a11.96 11.96 0 0 0 5.78 1.47h.01c6.58 0 11.94-5.35 11.95-11.94a11.87 11.87 0 0 0-3.48-8.41ZM12.05 21.8a9.9 9.9 0 0 1-5.04-1.38l-.36-.21-3.72.98.99-3.63-.24-.37a9.86 9.86 0 0 1-1.51-5.25c0-5.47 4.45-9.92 9.92-9.92a9.85 9.85 0 0 1 7.01 2.91 9.84 9.84 0 0 1 2.9 7.01c0 5.47-4.45 9.92-9.95 9.92Zm5.44-7.43c-.3-.15-1.77-.87-2.05-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.8-1.49-1.78-1.67-2.08-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.18.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.62-.92-2.22-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.8.37-.27.3-1.04 1.02-1.04 2.49 0 1.47 1.07 2.89 1.22 3.09.15.2 2.1 3.2 5.08 4.48.71.31 1.27.49 1.71.63.72.23 1.38.2 1.9.12.58-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.12-.27-.2-.57-.35Z"/></g>',
 'spark':f'<path d="{SPARK}" fill="var(--icon-accent,#ead28c)"/><path d="M9 23 6 26M24 6l2-2"/>',
 'brand':f'<path d="M6 11 22 6l5 17-16 5Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="m5 12 15-5 6 16-15 5ZM10 16l10-3M12 21l7-2"/><path d="M7 8 18 4"/><path d="{SMALL}" {ACCENT}/>',
 'voice':f'<path d="m6 13 15-7v18L6 19Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="m6 13 15-7v18L6 19ZM6 13H3v6h3M10 21l2 7h5l-3-9M25 12l4-2M25 20l4 2"/><path d="{SMALL}" {ACCENT}/>',
 'experience':f'<path d="M7 26V15a9 9 0 0 1 18 0v11" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="M7 26V15a9 9 0 0 1 18 0v11M12 26V15a4 4 0 0 1 8 0v11M3 27h26M5 30h22"/><path d="{SMALL}" {ACCENT}/>',
 'listen':f'<path d="M4 9a5 5 0 0 1 5-5h12a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H12l-7 5v-7a5 5 0 0 1-1-3Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="M4 9a5 5 0 0 1 5-5h12a5 5 0 0 1 5 5v8a5 5 0 0 1-5 5H12l-7 5v-7a5 5 0 0 1-1-3Z"/><circle cx="11" cy="13" r="1" fill="currentColor" stroke="none"/><circle cx="17" cy="13" r="1" fill="currentColor" stroke="none"/><path d="{SMALL}" {ACCENT}/>',
 'wand':f'<path d="m6 27 14-14 4 4-14 14Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="m4 25 15-15 4 4L8 29ZM15 14l4 4M6 8 4 6M12 5V2M28 21h3"/><path d="M24 2c.6 4.6 2.4 6.4 7 7-4.6.6-6.4 2.4-7 7-.6-4.6-2.4-6.4-7-7 4.6-.6 6.4-2.4 7-7Z" {ACCENT}/>',
 'launch':f'<path d="M4 14 28 4 18 28l-4-10Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="M4 14 28 4 18 28l-4-10ZM14 18 28 4M4 25l3-3M8 29l3-3"/><path d="M7 3c.3 2.4 1.6 3.7 4 4-2.4.3-3.7 1.6-4 4-.3-2.4-1.6-3.7-4-4 2.4-.3 3.7-1.6 4-4Z" {ACCENT}/>',
 'paper':f'<path d="M8 4h13l6 6v18H8Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="M8 4h13l6 6v18H8ZM21 4v7h6M12 16h10M12 21h7M4 8v20"/><path d="{SMALL}" {ACCENT}/>',
 'arrow':'<path d="M5 17h21M20 10l7 7-7 7M5 17c-2 0-2-4 0-4"/>',
 'up':'<path d="M7 25 25 7M12 7h13v13M7 25c-2 2-5-1-3-3"/>',
 'left':'<path d="M27 17H6M12 10l-7 7 7 7M27 17c2 0 2-4 0-4"/>',
 'pause':'<path d="M11 7v18M21 7v18"/>',
 'play-solid':'<path d="m11 6 15 10-15 10Z"/>',
 'close':'<path d="m8 8 16 16M8 24 24 8"/>',
 'plus':'<path d="M16 7v18M7 16h18"/>',
 'menu':'<path d="M5 11h22M5 21h22"/>',
 'check':'<path d="m7 17 6 6L26 9"/>',
 'mail':f'<path d="M4 8h24v18H4Z" fill="var(--icon-wash,#dff2ec)" stroke="none"/><path d="M4 8h24v18H4ZM4 8l12 11L28 8"/>',
}
ALIASES={'people':'listen','chevron':'arrow'}
LABELS={'brand':'Une identité à votre image','voice':'Une idée qui se fait entendre','experience':'Un moment qui prend vie','listen':'On vous écoute','wand':'On cherche la bonne idée','launch':'On lui donne vie','paper':'Le sens du détail','spark':'La touche Magic'}

def icon(name='arrow'):
 name=ALIASES.get(name,name)
 if name not in ICONS:raise ValueError(f'Unknown Magic icon: {name}')
 return f'<svg class="magic-icon icon-{name}" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><use href="/assets/magic-icons.svg#magic-{name}"/></svg>'

def write_sprite(root):
 root=Path(root);folder=root/'assets/icons';folder.mkdir(exist_ok=True)
 sprite='<svg xmlns="http://www.w3.org/2000/svg">'+''.join(f'<symbol id="magic-{name}" viewBox="0 0 32 32">{body}</symbol>' for name,body in ICONS.items())+'</svg>'
 (root/'assets/magic-icons.svg').write_text(sprite,encoding='utf-8')
 for name,body in ICONS.items():
  (folder/f'magic-{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="none" stroke="#062d26" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{body}</svg>',encoding='utf-8')
 preview='<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Les signes Magic — icônes originales</title><link rel="stylesheet" href="/assets/fonts/magic-fonts.css"><style>body{margin:0;padding:45px;background:#fffaf0;color:#062d26;font-family:Manrope,sans-serif}h1{font-size:42px;font-weight:500;letter-spacing:-.04em;margin:0}p{max-width:60ch;font-size:15px;line-height:1.8}main{max-width:1100px;margin:auto}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:16px;margin-top:35px}article{padding:28px;border:1px solid #062d2626;border-radius:12px}svg{width:68px;height:68px;margin-bottom:25px}h2{font-size:15px;font-weight:600}span{font-size:11px;opacity:.7}a{color:inherit}</style><main><h1>Les signes Magic.</h1><p>Une famille originale de formes, inspirée de la baguette et de l’étoile du logo. Des courbes nettes, un trait commun et une touche d’or.</p><div class="grid">'+''.join(f'<article>{icon(name)}<h2>{label}</h2><span>magic-{name}.svg</span></article>' for name,label in LABELS.items())+'</div><p><a href="/">Revenir au site</a></p></main></html>'
 (root/'website/icon-preview.html').write_text(preview,encoding='utf-8')
