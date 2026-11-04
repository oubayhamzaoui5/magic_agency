"""Reviewable service compositions; the selected homepage stays intact."""
from pathlib import Path
from hashlib import sha256
import re

ROOT = Path(__file__).resolve().parents[1]
VARIANTS = [('editorial', 'L’éditorial', 'Une liste ouverte, lisible et généreuse.'),
            ('panorama', 'Le panorama', 'Des expertises en grand, une composition asymétrique.'),
            ('parcours', 'Le fil de la marque', 'Une traversée verticale, du cap à la rencontre.')]
SERVICES = [
    dict(key='strategie', title='Stratégie', verb='Trouver votre cap.',
         desc='Votre public, votre place, votre façon de parler. On pose les bonnes questions pour donner une direction claire à la création.',
         items=['Positionnement', 'Messages & ton de voix', 'Plan de communication'], need='Clarifier ma stratégie'),
    dict(key='marque', title='Branding', verb='Donner du caractère.',
         desc='Un logo est un début. Couleurs, typographies, images et matières construisent une identité qu’on reconnaît partout.',
         items=['Identité visuelle', 'Packaging & édition', 'Direction artistique'], need='Construire ma marque'),
    dict(key='visibilite', title='Présence digitale', verb='Faire vivre votre univers.',
         desc='Un site clair pour vous découvrir. Des réseaux sociaux et des contenus photo, vidéo et motion qui gardent le même fil.',
         items=['Sites web & e-commerce', 'Social media', 'Photo, vidéo & motion'], need='Développer ma présence digitale'),
    dict(key='experience', title='Événements', verb='Créer la rencontre.',
         desc='Un concept, un lieu et tous les détails qui transforment votre idée en expérience. Des gens, un moment qui reste.',
         items=['Concept & scénographie', 'Lancements & activations', 'Invitations & signalétique'], need='Créer un événement / une activation'),
]


def build_service_variants(page, original_section, mark, image, icon):
    original_mark = mark
    mark = lambda key: original_mark(key).replace('loading="lazy"', 'loading="eager"')
    def cta(s):
        return f'<a class="sv-link" href="#contact" data-service-need="{s["need"]}">Parlons de votre {"événement" if s["key"] == "experience" else "projet"}{icon("up")}</a>'

    def tags(s):
        return '<ul class="sv-deliverables">'+''.join(f'<li>{item}</li>' for item in s['items'])+'</ul>'

    def event_image():
        return '<figure class="sv-event-image">'+image('muse-event', sizes='(min-width:1280px) 600px, 100vw')+'<figcaption>Concept événementiel fictif · image générée.</figcaption></figure>'

    intro = '<div class="sv-intro"><h2 id="services-title">De votre première idée<br><em>à votre prochaine rencontre.</em></h2><p>On clarifie ce que votre marque raconte. On lui donne une identité. Puis on la fait vivre, sur les écrans comme sur le terrain.</p></div>'
    foot = '<div class="sv-foot"><p>Un besoin précis ou un projet à 360° :<br>on construit le bon périmètre avec vous.</p><a class="button sv-contact" href="#contact">Parlons de votre projet<span class="button-icon">'+icon('up')+'</span></a></div>'
    for slug, name, description in VARIANTS:
        if slug == 'editorial':
            rows = ''
            for s in SERVICES:
                visual = event_image() if s['key'] == 'experience' else ''
                rows += f'<article class="sv-row" id="service-{s["key"]}"><div class="sv-name">{mark(s["key"])}<h3>{s["title"]}</h3></div><div class="sv-detail"><h4>{s["verb"]}</h4><p>{s["desc"]}</p>{tags(s)}{cta(s)}</div>{visual}</article>'
            content = intro+'<div class="sv-editorial-list">'+rows+'</div>'+foot
        elif slug == 'panorama':
            cells = ''
            for s in SERVICES[:3]:
                cells += f'<article class="sv-cell sv-cell--{s["key"]}" id="service-{s["key"]}">{mark(s["key"])}<div class="sv-cell-copy"><h3>{s["title"]}</h3><h4>{s["verb"]}</h4><p>{s["desc"]}</p>{tags(s)}{cta(s)}</div></article>'
            s = SERVICES[3]
            event = f'<article class="sv-event" id="service-experience"><div class="sv-event-copy">{mark(s["key"])}<h3>{s["title"]}</h3><h4>{s["verb"]}</h4><p>{s["desc"]}</p>{tags(s)}{cta(s)}</div>{event_image()}</article>'
            content = intro+'<div class="sv-panorama-grid">'+cells+'</div>'+event+foot
        else:
            rows = ''
            for s in SERVICES:
                visual = event_image() if s['key'] == 'experience' else ''
                rows += f'<article class="sv-chapter" id="service-{s["key"]}"><div class="sv-chapter-mark">{mark(s["key"])}</div><div class="sv-chapter-copy"><p class="sv-service-name">{s["title"]}</p><h3>{s["verb"]}</h3><p>{s["desc"]}</p>{tags(s)}{cta(s)}{visual}</div></article>'
            content = '<div class="sv-journey-layout">'+intro+'<div class="sv-chapters">'+rows+'</div></div>'+foot
        section = f'<section class="sv-services sv-{slug}" id="services" aria-labelledby="services-title"><div class="container">{content}</div></section>'
        if slug == 'editorial':
            from editorial_services import render_editorial_services
            section = render_editorial_services(mark, icon)
        links = ''.join(f'<a href="/directions/services-{key}/#services"'+(' aria-current="page"' if key == slug else '')+f'>{label}</a>' for key, label, _ in VARIANTS)
        review = '<aside class="sv-review" aria-label="Comparer les propositions"><span>Services · 3 propositions</span><nav aria-label="Propositions de section">'+links+'</nav><a href="/">Retour au site</a></aside>'
        result = page.replace(original_section, section)
        result = result.replace('content="index, follow"', 'content="noindex, follow"')
        result = result.replace('</head>', '<link rel="stylesheet" href="/assets/service-variants.css?v='+sha256((ROOT/'assets/service-variants.css').read_bytes()).hexdigest()[:12]+'"></head>')
        if slug != 'editorial':
            result = result.replace('</body>', review+'</body>')
        result = re.sub(r'<title>.*?</title>', f'<title>{name} — Proposition services | Magic 360</title>', result)
        target = ROOT/'directions'/('services-'+slug)/'index.html'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(result.replace('><', '>\n<'), encoding='utf-8')


if __name__ == '__main__':
    from build_magic import service_content, service_mark, img, icon
    build_service_variants((ROOT/'index.html').read_text(encoding='utf-8').replace('>\n<', '><'), service_content(), service_mark, img, icon)
