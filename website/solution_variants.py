"""Three reviewable solutions sections, inserted after the accepted services."""
from pathlib import Path
from hashlib import sha256
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
VARIANTS = [('atelier', 'L’atelier digital'), ('editorial', 'L’éditorial'), ('connexions', 'Les connexions')]
SOLUTIONS = [
    dict(id='plateformes', title='Plateformes sur mesure', line='Votre activité. Votre propre outil.',
         text='Un portail client, un espace partenaire ou un outil de gestion interne. On conçoit une plateforme autour de vos équipes, de vos données et de votre façon de travailler.',
         examples=['Portails clients & partenaires', 'Outils métier & tableaux de bord', 'Espaces de gestion centralisés'],
         problem='Tout est éparpillé ?', answer='Un espace qui rassemble.', need='Créer une plateforme sur mesure'),
    dict(id='automatisations', title='Automatisations', line='Les bonnes actions, sans les répétitions.',
         text='Relier vos outils et faire circuler l’information. Demandes, notifications, relances ou synchronisations : on imagine les enchaînements qui simplifient votre quotidien.',
         examples=['Suivi des demandes', 'Notifications & relances', 'Synchronisation entre outils'],
         problem='Encore la même tâche ?', answer='Un processus qui avance.', need='Automatiser mes processus'),
    dict(id='applications', title='Applications', line='L’essentiel, à portée de main.',
         text='Une application web ou mobile pensée pour un usage précis. Réserver, commander, consulter ou travailler sur le terrain : une expérience simple, adaptée à ses utilisateurs.',
         examples=['Applications web & mobiles', 'Réservation & commande', 'Outils pour les équipes terrain'],
         problem='Votre outil vous freine ?', answer='Une application qui vous suit.', need='Développer une application'),
]


def portal(icon):
    return f'''<div class="sl-portal sl-demo" role="img" aria-label="Interface illustrative d’un portail client : projets, documents et prochaines étapes réunis dans un espace."><div class="sl-window"><span class="sl-window-dots" aria-hidden="true"><i></i><i></i><i></i></span><span>votre-espace</span><span class="sl-avatar">M</span></div><div class="sl-portal-body"><div class="sl-sidebar"><strong>Votre espace<span>.</span></strong><span class="sl-nav-active">Vue d’ensemble</span><span>Mes projets</span><span>Documents</span><span>Messages</span><small>Tout commence ici.</small></div><div class="sl-dashboard"><p class="sl-greeting">Bonjour, Lina.</p><strong>On fait le point ?</strong><div class="sl-project"><div><span>Votre projet</span><b>Une nouvelle<br>identité à déployer.</b></div><span class="sl-status">En cours</span></div><div class="sl-mini-heading"><b>Les prochaines étapes</b><span>Cette semaine</span></div><div class="sl-task">{icon('check')}<span>Valider la direction créative</span><small>Fait</small></div><div class="sl-task">{icon('paper')}<span>Retrouver les derniers fichiers</span>{icon('up')}</div><div class="sl-task">{icon('brand')}<span>Préparer le lancement</span>{icon('up')}</div></div></div></div>'''


def flow(icon):
    return f'''<div class="sl-flow sl-demo" role="img" aria-label="Exemple illustratif d’automatisation : une demande reçue crée une fiche, notifie l’équipe et prépare une relance."><span class="sl-flow-label">Une demande arrive.</span><div class="sl-flow-step sl-trigger">{icon('mail')}<span><small>Déclencheur</small><b>Nouveau formulaire reçu</b></span><span class="sl-live-dot" aria-hidden="true"></span></div><div class="sl-flow-line" aria-hidden="true"></div><div class="sl-flow-step">{icon('paper')}<span><small>Votre outil de suivi</small><b>Une fiche est créée</b></span>{icon('check')}</div><div class="sl-flow-line" aria-hidden="true"></div><div class="sl-flow-step">{icon('voice')}<span><small>Votre équipe</small><b>La bonne personne est informée</b></span>{icon('check')}</div><div class="sl-flow-line" aria-hidden="true"></div><div class="sl-flow-step sl-flow-last">{icon('spark')}<span><small>La suite se prépare</small><b>Une relance est planifiée</b></span></div><span class="sl-flow-note">Vous gardez la main sur les règles.</span></div>'''


def app(icon):
    return f'''<div class="sl-app-scene sl-demo" role="img" aria-label="Interface illustrative d’une application de réservation sur téléphone, avec service, date et créneau."><div class="sl-app-orbit" aria-hidden="true"></div><div class="sl-phone"><div class="sl-phone-top"><span>9:41</span><span class="sl-phone-notch" aria-hidden="true"></span><span>4G</span></div><div class="sl-phone-content"><span class="sl-app-brand">À votre rythme{icon('spark')}</span><strong>Votre prochain<br>rendez-vous.</strong><p>Choisissez le moment qui vous va.</p><div class="sl-booking"><span>Votre séance</span><b>Un temps pour vous.</b><small>45 min · Sur place</small></div><div class="sl-week"><span>Lun<b>12</b></span><span>Mar<b>13</b></span><span class="sl-day-active">Mer<b>14</b></span><span>Jeu<b>15</b></span><span>Ven<b>16</b></span></div><div class="sl-times"><span>09:00</span><span class="sl-time-active">10:30</span><span>14:00</span></div><span class="sl-app-button">Choisir ce créneau{icon('up')}</span></div></div><span class="sl-app-sticker">Simple.<br>Utile.<br>À vous.</span></div>'''


def solution_sections(icon):
    visuals = [portal(icon), flow(icon), app(icon)]
    sections = {}

    def cta(s):
        return f'<a class="sl-link" href="#contact" data-service-need="{escape(s["need"])}">Parlons de votre besoin{icon("up")}</a>'

    def copy(s, heading='h3'):
        return f'<{heading}>{s["title"]}</{heading}><p class="sl-line">{s["line"]}</p><p class="sl-description">{s["text"]}</p><ul class="sl-examples">'+''.join(f'<li>{item}</li>' for item in s['examples'])+'</ul>'+cta(s)

    for slug, label in VARIANTS:
        if slug == 'atelier':
            intro = '<div class="sl-intro"><h2 id="solutions-title">Votre façon de travailler.<br><em>Vos propres outils.</em></h2><p>La bonne solution ne vous oblige pas à changer vos habitudes. Elle se construit autour de votre activité.</p></div>'
            first = f'<article class="sl-featured"><div class="sl-copy">{copy(SOLUTIONS[0])}</div><div class="sl-visual">{visuals[0]}</div></article>'
            rest = ''.join(f'<article class="sl-half"><div class="sl-visual">{visuals[i]}</div><div class="sl-copy">{copy(SOLUTIONS[i])}</div></article>' for i in [1, 2])
            content = intro+first+'<div class="sl-halves">'+rest+'</div>'
        elif slug == 'editorial':
            intro = '<div class="sl-intro"><h2 id="solutions-title">Des solutions qui font<br><em>avancer votre quotidien.</em></h2><p>Plateformes métier, automatisations, applications. On part de votre besoin pour concevoir un outil qui trouve sa place dans votre activité.</p></div>'
            rows = ''.join(f'<article class="sl-row sl-row--{s["id"]}"><div class="sl-copy">{copy(s)}</div><div class="sl-visual">{visuals[i]}</div></article>' for i,s in enumerate(SOLUTIONS))
            content = intro+'<div class="sl-rows">'+rows+'</div>'
        else:
            intro = '<div class="sl-intro"><h2 id="solutions-title">Moins de friction.<br><em>Plus de possibilités.</em></h2><p>Ce qui vous ralentit aujourd’hui peut devenir votre prochain outil. Ensemble, on relie vos besoins à des solutions concrètes.</p></div>'
            rows = ''.join(f'<article class="sl-connection"><div class="sl-problem"><p>{s["problem"]}</p>{icon("arrow")}</div><div class="sl-answer"><h3>{s["answer"]}</h3><p class="sl-solution-name">{s["title"]}</p><p class="sl-description">{s["text"]}</p>{cta(s)}</div><div class="sl-visual">{visuals[i]}</div></article>' for i,s in enumerate(SOLUTIONS))
            content = intro+'<div class="sl-connections">'+rows+'</div>'
        end = f'<div class="sl-finale"><p>Un outil à imaginer ?<br><strong>Commençons par votre quotidien.</strong></p><a href="#contact" class="button sl-contact" data-service-need="Plusieurs besoins / à définir">Construisons votre solution<span class="button-icon">{icon("up")}</span></a></div><p class="sl-disclosure">Interfaces illustratives · exemples de solutions, sans données réelles.</p>'
        section = f'<section class="solutions sl-{slug}" id="solutions" aria-labelledby="solutions-title"><div class="container">{content}{end}</div></section>'
        sections[slug] = section
    return sections


def apply_solution(page, section):
    result = page.replace('<section class="agency section"', section+'<section class="agency section"', 1)
    css_hash = sha256((ROOT/'assets/solution-variants.css').read_bytes()).hexdigest()[:12]
    result = result.replace('</head>',f'<link rel="stylesheet" href="/assets/solution-variants.css?v={css_hash}"></head>')
    options = ''.join(f'<option>{s["need"]}</option>' for s in SOLUTIONS)
    return result.replace('<option>Plusieurs besoins / à définir</option>', options+'<option>Plusieurs besoins / à définir</option>')


def build_solution_variants(page, icon):
    sections = solution_sections(icon)
    for slug, label in VARIANTS:
        result = apply_solution(page, sections[slug])
        links = ''.join(f'<a href="/directions/solutions-{key}/#solutions"'+(' aria-current="page"' if key == slug else '')+f'>{name}</a>' for key,name in VARIANTS)
        review = '<aside class="sl-review" aria-label="Comparer les sections solutions"><span>Solutions · 3 propositions</span><nav aria-label="Propositions de solutions">'+links+'</nav><a href="/">Retour au site</a></aside>'
        result = result.replace('</body>',review+'</body>')
        result = re.sub(r'<title>.*?</title>',f'<title>{label} — Solutions | Magic 360</title>',result)
        target = ROOT/'directions'/('solutions-'+slug)/'index.html'
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(result.replace('><','>\n<'),encoding='utf-8')
