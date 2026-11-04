"""Selected service section: four editorial groups, twelve distinct service stories."""
from html import escape

GROUPS = [
    dict(key='strategie', title='Stratégie', verb='Trouver votre cap.',
         desc='Avant de créer, trouver ce qui vous distingue. Votre public, votre place, votre façon de parler : on donne une direction claire à la création.',
         need='Clarifier ma stratégie', services=[
             ('positionnement', 'Positionnement', 'Faire émerger votre singularité, comprendre vos publics et définir la place que votre marque veut prendre.', 'Composition de marque : documents, portraits de publics et objet bleu sur fond vert forêt.'),
             ('messages', 'Messages & ton de voix', 'Choisir les mots, les messages et la personnalité qui rendent votre marque reconnaissable, à chaque prise de parole.', 'Trois compositions typographiques sur papier ivoire, bleu et lime : Bonjour, Et si, Ensemble.'),
             ('plan-communication', 'Plan de communication', 'Relier vos objectifs aux bons canaux et organiser vos prises de parole dans un calendrier cohérent.', 'Un chemin de papier relie les trois temps d’une campagne de communication.')]),
    dict(key='marque', title='Branding', verb='Donner du caractère.',
         desc='Une identité qui se reconnaît, jusque dans les détails. On relie les couleurs, les formes, les mots et les matières pour faire exister votre univers.',
         need='Construire ma marque', services=[
             ('identite-visuelle', 'Identité visuelle', 'Logo, couleurs, typographies et règles d’usage : une base claire pour déployer votre marque avec cohérence.', 'Concept VELA : manuel d’identité, cartes et enveloppe dans un univers forêt, ivoire et abricot.'),
             ('packaging-edition', 'Packaging & édition', 'Des emballages aux supports imprimés, donner une forme tangible à votre identité et soigner chaque point de contact.', 'Concept VELA : flacon ambré, coffret vert forêt et livret en papier texturé.'),
             ('direction-artistique', 'Direction artistique', 'Définir un parti pris visuel et le faire vivre dans vos campagnes, vos images et vos supports de lancement.', 'Concept VELA : affiche de campagne, flacon et lumière ambrée dans une composition sculpturale.')]),
    dict(key='visibilite', title='Présence digitale', verb='Faire vivre votre univers.',
         desc='Votre marque en ligne, avec quelque chose à raconter. Des expériences utiles et des contenus qui gardent le même fil, du premier clic à la prochaine publication.',
         need='Développer ma présence digitale', services=[
             ('sites-web', 'Sites web & e-commerce', 'Présenter votre activité, guider vos visiteurs et faciliter l’achat avec un site clair, pensé pour les écrans du quotidien.', 'Concept ONDA : boutique en ligne sur un écran, canette bleue et citron vert sur un décor cobalt.'),
             ('social-media', 'Social media', 'Une ligne éditoriale, des formats reconnaissables et un calendrier de contenus pour animer votre marque sur les réseaux.', 'Concept ONDA : campagne social media sur téléphone et créations graphiques cobalt, lime et abricot.'),
             ('photo-video-motion', 'Photo, vidéo & motion', 'Des images fixes aux formats animés, produire les contenus qui donnent du relief à votre univers et racontent votre offre.', 'Concept ONDA : tournage produit avec caméra, canette cobalt et citron sur un décor lime.')]),
    dict(key='experience', title='Événements', verb='Créer la rencontre.',
         desc='Des gens. Un lieu. Un moment qui reste. On transforme votre idée en expérience, du concept aux détails qui accueillent votre public.',
         need='Créer un événement / une activation', services=[
             ('scenographie', 'Concept & scénographie', 'Imaginer le fil conducteur, dessiner l’espace et composer une ambiance qui donne corps à votre marque.', 'Concept MUSE : arche sculpturale bleue et bannières lime dans une cour méditerranéenne.'),
             ('muse-event', 'Lancements & activations', 'Faire vivre votre lancement ou votre rencontre B2B à travers une expérience pensée pour votre public.', 'Concept MUSE : visiteurs réunis dans une cour, sculpture bleue et signalétique jaune.'),
             ('invitations-signaletique', 'Invitations & signalétique', 'De l’invitation aux repères sur place, créer les supports qui donnent envie de venir et accompagnent la rencontre.', 'Concept MUSE : invitation abricot, programme, badge et signalétique directionnelle.')]),
]


def render_editorial_services(mark, icon):
    groups = []
    for group in GROUPS:
        features = []
        for key, title, description, alt in group['services']:
            legacy = key == 'muse-event'
            folder = 'magic' if legacy else 'services'
            widths = (480, 900, 1400) if legacy else (480, 800, 1200)
            source = f'/assets/{folder}/{key}-{widths[0]}.webp'
            srcset = ', '.join(f'/assets/{folder}/{key}-{w}.webp {w}w' for w in widths)
            features.append(f'''<article class="es-feature" id="expertise-{key}" aria-labelledby="title-{key}"><figure><img src="{source}" srcset="{srcset}" sizes="(min-width:1650px) 515px, (min-width:1280px) 384px, (min-width:768px) calc((100vw - 112px)/3), calc(100vw - 32px)" width="1536" height="1024" alt="{escape(alt)}" loading="lazy" decoding="async"></figure><h4 id="title-{key}">{escape(title)}</h4><p>{escape(description)}</p></article>''')
        groups.append(f'''<section class="es-group" id="service-{group['key']}" aria-labelledby="group-{group['key']}"><header class="es-group-heading"><div class="es-name">{mark(group['key'])}<div><h3 id="group-{group['key']}">{group['title']}</h3><p>{group['verb']}</p></div></div><div class="es-summary"><p>{group['desc']}</p><a class="es-link" href="#contact" data-service-need="{escape(group['need'])}">Parlons de votre {'événement' if group['key'] == 'experience' else 'projet'}{icon('up')}</a></div></header><div class="es-features">{''.join(features)}</div></section>''')
    return '''<section class="editorial-services" id="services" aria-labelledby="services-title"><div class="container"><div class="es-intro"><h2 id="services-title">De votre première idée<br><em>à votre prochaine rencontre.</em></h2><p>Une direction, une identité, une présence.<br>Et tous les savoir-faire pour leur donner vie.</p></div>'''+''.join(groups)+f'''<div class="es-finale"><p>Un besoin précis ou un projet à 360° :<br>on construit le bon périmètre avec vous.</p><a class="button es-contact" href="#contact">Parlons de votre projet<span class="button-icon">{icon('up')}</span></a></div><p class="es-disclosure">Visuels de démonstration générés · marques et projets fictifs.</p></div></section>'''
