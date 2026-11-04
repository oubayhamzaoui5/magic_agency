"""Magic in motion. Build the current homepage; archive builder stays independent."""
from pathlib import Path
from html import escape
from hashlib import sha256
import json
from magic_icons import icon, write_sprite
from hero_content import render_lanes

ROOT=Path(__file__).resolve().parent.parent
WORK={
'naya':{'title':'Naya','category':'branding','label':'Identité & direction artistique','description':'Une marque de soin qui ose la couleur. Une identité, une direction produit et un langage visuel imaginés pour les mêmes moments de marque.','deliverables':['Identité visuelle','Direction artistique','Campagne produit'],'alt':'Concept Naya : soins lavande et bleu cobalt'},
'kora':{'title':'Kora','category':'campagne','label':'Campagne & image de marque','description':'Du mouvement dans l’image. Une exploration de campagne sport où la photographie produit et la typographie portent la même énergie.','deliverables':['Concept de campagne','Création publicitaire','Direction photo'],'alt':'Concept Kora : sneaker bleue sur une composition rouge et ivoire'},
'packaging':{'title':'Zéra','category':'branding','label':'Branding & packaging','description':'Une huile d’olive imaginaire, un ancrage méditerranéen. De l’identité au coffret, chaque détail appartient au même univers.','deliverables':['Identité visuelle','Packaging','Direction photo'],'alt':'Concept Zéra : bouteilles d’huile d’olive et coffrets vert et ivoire'},
'event':{'title':'Rencontres','category':'experience','label':'Scénographie & activation','description':'Une expérience de marque pensée dans l’espace. Architecture, lumière et mise en scène explorent un lancement au bord de la Méditerranée.','deliverables':['Concept événementiel','Scénographie','Activation'],'alt':'Concept Rencontres : lancement imaginaire dans une cour au crépuscule'},
'saison':{'title':'Saison','category':'branding','label':'Packaging & campagne produit','description':'Un lancement plein de caractère. Un système de packaging et des images de campagne qui donnent le goût de découvrir la marque.','deliverables':['Design packaging','Campagne produit','Contenus sociaux'],'alt':'Concept Saison : canettes et oranges sur une composition corail'},
'digital':{'title':'Soli','category':'digital','label':'Digital & social media','description':'Du produit au téléphone, la même idée. Une campagne fictive de boisson déclinée en images et en contenus sociaux.','deliverables':['Concept social','Création de contenu','Visuels produit'],'alt':'Concept Soli : boisson au citron et campagne sur smartphone'},
'muse':{'title':'Muse','category':'campagne','label':'Culture & affichage','description':'Un festival d’art fictif, une présence qui se remarque. La typographie et la matière deviennent un langage d’affichage cohérent.','deliverables':['Identité culturelle','Affichage','Campagne'],'alt':'Concept Muse : affiches culturelles avec sculpture bleue'},
'hospitality':{'title':'Maison Nūr','category':'branding','label':'Identité & édition','description':'L’hospitalité jusque dans les supports. Un univers fictif décliné en menu, papeterie et objets d’accueil.','deliverables':['Identité','Édition','Papeterie'],'alt':'Concept Maison Nūr : menu et papeterie hôtelière'},
'campaign':{'title':'Horizon','category':'campagne','label':'Affichage & communication','description':'Le son, la mer, la vie. Une campagne culturelle imaginaire conçue pour se reconnaître dans la rue et sur les écrans.','deliverables':['Communication','Affichage','Direction artistique'],'alt':'Concept Horizon : affiche de festival dans une rue méditerranéenne'}
}
WORK.update({
 'pulse':{'title':'Pulse','category':'campagne','label':'Identité & campagne produit','description':'Un casque, une couleur, une présence. Une exploration où le bleu électrique et le jaune donnent une personnalité immédiate à un objet du quotidien.','deliverables':['Identité visuelle','Packaging','Campagne produit'],'alt':'Concept Pulse : casque bleu cobalt et packaging jaune et bleu'},
 'grain':{'title':'Grain','category':'branding','label':'Packaging & direction artistique','description':'Du papier froissé, un café et une couleur chaude. Une identité de café fictive pensée pour garder quelque chose de simple et de vivant dans chaque détail.','deliverables':['Identité de marque','Packaging','Direction photo'],'alt':'Concept Grain : sachets de café orange, tasse et main tenant un emballage'},
 'palma':{'title':'Palma','category':'campagne','label':'Image de marque & campagne','description':'Une lumière franche, de l’eau et un geste naturel. Un concept solaire où le produit entre dans une scène plutôt que de rester posé à côté.','deliverables':['Direction artistique','Photographie de campagne','Création publicitaire'],'alt':'Concept Palma : soins solaires corail et turquoise au bord d’une piscine'}
})
WORK.update({
 'grain-strategy':{'title':'Grain, du fond à la forme','category':'strategie','label':'Stratégie & identité de marque','description':'Exemple fictif : lancer un café de spécialité. Partir du public et de la personnalité de la marque, puis traduire ce cap en couleurs, en mots et en packaging.','deliverables':['Positionnement','Territoire de marque','Identité & packaging'],'alt':'Concept Grain : main disposant des nuanciers, un sachet de café orange et des supports de marque'},
 'palma-digital':{'title':'Palma, sur tous les écrans','category':'digital','label':'Site web & social media','description':'Exemple fictif : faire vivre une marque de soin en ligne. Un site pour découvrir les produits, une direction de contenu pour les réseaux sociaux et des visuels qui gardent la même personnalité.','deliverables':['Direction digitale','Site e-commerce','Contenus social media'],'alt':'Concept Palma : site e-commerce sur ordinateur, contenus sociaux sur téléphone et tube de soin corail'},
 'muse-event':{'title':'Muse, une marque qui se vit','category':'experience','label':'Événement & expérience de marque','description':'Exemple fictif : donner rendez-vous autour d’un lancement culturel. Une idée de scénographie relie l’invitation, la signalétique, l’installation et les moments de rencontre.','deliverables':['Concept événementiel','Scénographie','Invitations & signalétique'],'alt':'Concept Muse : visiteurs dans une cour méditerranéenne, sculpture bleue et signalétique jaune'}
})
NEW={'naya','kora','saison','muse','magic-object','pulse','grain','palma','creative-table','grain-strategy','palma-digital','muse-event'}
for retired in ['packaging','event','digital','hospitality','campaign']:
 WORK.pop(retired,None)
NEW.update({'naya-hands','naya-campaign','kora-campaign','pulse-lifestyle','saison-campaign','palma-campaign'})
ALBUMS={
 'naya':['naya','naya-hands','naya-campaign'],
 'kora':['kora','kora-campaign'],
 'saison':['saison','saison-campaign'],
 'pulse':['pulse','pulse-lifestyle'],
 'palma-digital':['palma','palma-digital','palma-campaign'],
 'palma':['palma','palma-digital','palma-campaign'],
 'grain-strategy':['grain-strategy','grain'],
 'grain':['grain','grain-strategy'],
 'muse-event':['muse','muse-event'],
 'muse':['muse','muse-event']
}
ASSET_ALTS={
 'naya-hands':'Concept Naya : mains utilisant le tube lavande et le pot de crème bleu cobalt',
 'naya-campaign':'Concept Naya : affiche lavande, packaging et guide de marque',
 'kora-campaign':'Concept Kora : geste de laçage, sneakers bleues et campagne rouge et crème',
 'pulse-lifestyle':'Concept Pulse : portrait de campagne avec casque bleu et univers jaune',
 'saison-campaign':'Concept Saison : main tenant une canette et campagne orange et vert',
 'palma-campaign':'Concept Palma : tote bag, carte de campagne et soins corail et turquoise'
}
ASSET_CAPTIONS={}
more_assets=ROOT/'website'/'MORE-CAMPAIGN-ASSETS.json'
if more_assets.exists():
 for asset in json.loads(more_assets.read_text(encoding='utf-8'))['assets']:
  NEW.add(asset['name'])
  ASSET_ALTS[asset['name']]=asset['alt']
  ASSET_CAPTIONS[asset['name']]=asset['caption']
  for album in ALBUMS.values():
   if asset['brand'] in album and asset['name'] not in album:
    album.append(asset['name'])
for key,project in WORK.items():
 project['images']=[{'key':asset,'alt':ASSET_ALTS.get(asset,WORK.get(asset,project)['alt'])} for asset in ALBUMS.get(key,[key])]
ART_NOTES={
 'naya':'Le parti pris : une couleur franche, une typographie sans détour.',
 'kora':'Faire sentir le mouvement, même à l’arrêt.',
 'packaging':'Une matière, une lumière, un ancrage méditerranéen.'
}
def img(key,cls='',eager=False,sizes='(min-width: 900px) 50vw, 100vw',decorative=False):
 folder='magic' if key in NEW else 'concepts';special_alt={'creative-table':'Scène de création imaginée : mains, essais papier et emballages fictifs sur une table'};alt='' if decorative else ASSET_ALTS.get(key,WORK.get(key,{'alt':special_alt.get(key,'Composition créative illustrative')})['alt'])
 return f'<img class="{cls}" src="/assets/{folder}/{key}-480.webp" srcset="/assets/{folder}/{key}-480.webp 480w, /assets/{folder}/{key}-900.webp 900w, /assets/{folder}/{key}-1400.webp 1400w" sizes="{sizes}" width="1536" height="1024" alt="{alt}" loading="{"eager" if eager else "lazy"}" decoding="async">'
def button(text,href='#contact',cls='button',arrow='up'):
 return f'<a class="{cls}" href="{href}"><span>{text}</span><span class="button-icon">{icon(arrow)}</span></a>'
def logo():
 return '<a class="brand" href="#top" aria-label="Magic 360 — accueil"><img src="/assets/magic/magic-logo.png" alt="Magic" width="352" height="160"></a>'
def tile(key,duplicate=False):
 p=WORK.get(key,{'title':key.split('-')[0].capitalize()});picture=img(key,eager=True,sizes='(min-width:900px) 210px, 180px',decorative=True)
 return f'<div class="wall-tile wall-tile-{key}">{picture}<span>{p["title"]}</span></div>'
def wall():
 return '<div class="campaign-wall" aria-label="Mur de concepts créatifs"><div class="wall-stage wall-stage--desktop" aria-hidden="true">'+render_lanes()+'</div><div class="wall-stage wall-stage--mobile" aria-hidden="true">'+render_lanes(mobile=True)+'</div><div class="wall-bottom"><button class="motion-control" aria-pressed="false" aria-label="Mettre le mouvement en pause">'+icon('pause')+'</button></div></div>'
def card(key):
 p=WORK[key]
 briefs={'pulse':'Donner un visage et une voix à un produit audio.','naya':'Donner une personnalité à une marque de soin.','kora':'Lancer une collection avec une campagne qui bouge.','grain-strategy':'Transformer un positionnement en univers de marque.','palma-digital':'Relier le site, les réseaux et le produit.','muse-event':'Faire vivre un lancement au-delà de l’affiche.','saison':'Décliner une idée du packaging aux contenus.'}
 note=f'<p class="work-note">{briefs.get(key,ART_NOTES.get(key,""))}</p><ul class="work-deliverables">'+''.join(f'<li>{escape(item)}</li>' for item in p['deliverables'])+'</ul>'
 album=ALBUMS.get(key,[key]);alternates=''.join(f'<button data-project="{key}" data-image-index="{i}" aria-label="Voir {p["title"]}, image {i+1} sur {len(album)}">{img(asset,sizes="(min-width:1000px) 24vw, 45vw")}<span>{ASSET_CAPTIONS.get(asset,["Le concept","La marque en situation","Les déclinaisons"][min(i,2)])} {icon("up")}</span></button>' for i,asset in enumerate(album) if i>0)
 return f'<article class="work-card" data-category="{p["category"]}"><button class="work-open" data-project="{key}" aria-label="Explorer le concept {p["title"]}"><span class="work-image">{img(album[0])}</span><span class="work-caption"><strong>{p["title"]}</strong><span>{p["label"]}</span><span class="work-arrow">{icon("up")}</span></span></button><p class="work-concept">Concept fictif · {len(album)} images</p>{note}<div class="work-alternates">{alternates}</div></article>'
def partners():
 logos=json.loads((ROOT/'website/PARTNER-OPTIONS.json').read_text(encoding='utf-8'))['partners']
 rows=[]
 for index,subset in enumerate([logos[:6],logos[6:]]):
  groups=[]
  for duplicate in [False,True]:
   items=[]
   for partner in subset:
    name='' if duplicate else escape(partner['name'],quote=True)
    tall=' partner-logo--tall' if partner['id'] in ['hm','iecd-tunisie','pharmacie-centrale-tunisie','cnci'] else ''
    items.append(f'<li class="partner-logo{tall}" data-partner="{partner["id"]}"><img src="{partner["ribbonAsset"]}" alt="{name}" width="{partner["width"]}" height="{partner["height"]}" loading="lazy" decoding="async"></li>')
   hidden=' aria-hidden="true"' if duplicate else ''
   groups.append(f'<ul class="partner-logo-group"{hidden}>'+''.join(items)+'</ul>')
  reverse=' partner-row--reverse' if index else ''
  rows.append(f'<div class="partner-row{reverse}">'+''.join(groups)+'</div>')
 return '<section class="partners partners--ribbons" id="partenaires" aria-labelledby="partners-title"><div class="container partners-inner"><div class="partners-heading"><h2 id="partners-title">Ils nous font confiance.</h2><p>Les partenaires de Magic 360</p></div><div class="partner-ribbons">'+''.join(rows)+'</div></div></section>'
def brand_story():
 options=json.loads((ROOT/'website/ABOUT-SECTION-OPTIONS.json').read_text(encoding='utf-8'))
 copy=options['copy']
 selected=next(concept for concept in options['concepts'] if concept['id']==options['selectedConceptId'])
 images=selected['responsiveAssets']
 heading=escape(copy['headingLines'][0])+'<br><em>'+escape(copy['headingLines'][1])+'</em>'
 return f'''<section class="brand-story" id="notre-approche" aria-labelledby="brand-story-title"><div class="container brand-story-layout"><div class="brand-story-copy"><p class="brand-story-label">{escape(copy['label'])}</p><h2 id="brand-story-title">{heading}</h2><p class="brand-story-statement">{escape(copy['subheading'])}</p><p class="brand-story-description">{escape(copy['body'])}</p>{button(copy['cta'],href=copy['target'],cls='button brand-story-cta')}</div><figure class="brand-story-visual"><img src="{images['900']}" srcset="{images['480']} 480w, {images['900']} 900w, {images['1254']} 1254w" sizes="(min-width:1650px) 764px, (min-width:1280px) 576px, (min-width:768px) calc(100vw - 64px), calc(100vw - 32px)" width="1254" height="1254" alt="Concept créatif : un homme sort d’un grand cadre vert, entre des sculptures de papier lime et ivoire." loading="lazy" decoding="async"><figcaption>Illustration créative · image générée.</figcaption></figure></div></section>'''

def service_panel(id,title,desc,key,items,example,need):
 return f'<section class="service-panel" id="service-{id}" role="tabpanel" aria-labelledby="tab-{id}" tabindex="0" data-need="{need}"><div class="service-visual">{img(key,sizes="(min-width:1000px) 55vw, 100vw")}<span class="concept-badge">Concept illustratif</span></div><div class="service-copy"><h3>{title}</h3><p>{desc}</p><div class="service-example"><strong>Par exemple</strong><p>{example}</p></div><div class="service-delivery"><strong>Ce qu’on crée ensemble</strong><ul>'+''.join(f'<li>{icon("check")}{item}</li>' for item in items)+f'</ul></div>{button("Parlons de ce besoin",cls="text-link")}</div></section>'
def service_mark(key):
 asset=key if key=='strategie' else key+'-v2'
 return f'<span class="service-mark"><img src="/assets/service-icons/{asset}-144.png" srcset="/assets/service-icons/{asset}-144.png 144w, /assets/service-icons/{asset}-288.png 288w" sizes="(min-width:1350px) 64px, (min-width:600px) 56px, 48px" width="144" height="144" alt="" loading="lazy" decoding="async"></span>'

def legacy_service_content():
 tabs=[('strategie','Stratégie','Trouver votre cap','listen'),('marque','Branding','Donner du caractère','brand'),('visibilite','Présence digitale','Site web & social media','voice'),('experience','Événements','Créer la rencontre','experience')]
 return '<section class="services section" id="services"><div class="container"><div class="section-heading service-heading"><h2>De votre première idée<br><em>à votre prochaine rencontre.</em></h2><p>On clarifie ce que votre marque raconte. On lui donne une identité. Puis on la fait vivre, sur les écrans comme sur le terrain.</p></div><div class="service-layout"><div class="service-tabs" role="tablist" aria-label="Explorer nos quatre expertises">'+''.join(f'<button role="tab" id="tab-{key}" aria-controls="service-{key}" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}">{service_mark(key)}<span class="service-tab-text">{title}<small>{desc}</small></span>{icon("up")}</button>' for i,(key,title,desc,symbol) in enumerate(tabs))+'</div><div class="service-panels">'+service_panel('strategie','Avant de créer,<br>trouver ce qui vous distingue.',"Votre public, votre place, votre façon de parler. On pose les bonnes questions pour donner une direction claire à la création.",'grain-strategy',['Positionnement & plateforme de marque','Publics, messages & ton de voix','Stratégie de communication & plan d’action'],"Vous lancez un café ? On définit à qui il s’adresse, ce qui le rend singulier et comment le raconter.",'Clarifier ma stratégie')+service_panel('marque','Une identité qu’on reconnaît.<br>Et qu’on a envie de retrouver.',"Un logo est un début. Couleurs, typographies, images, mots et matières construisent une marque cohérente, jusque dans les petits détails.",'naya',['Identité visuelle & charte graphique','Packaging, édition & supports de marque','Direction artistique & campagne de lancement'],"Une gamme de soins : une identité qui se retrouve sur le pot, le coffret et les images de campagne.",'Construire ma marque')+service_panel('visibilite','Votre marque en ligne.<br>Avec quelque chose à raconter.',"Un site clair pour vous découvrir. Des réseaux sociaux qui font vivre votre univers. Des contenus photo, vidéo et motion qui gardent le même fil.",'palma-digital',['Sites vitrines & e-commerce','Stratégie social media & calendrier éditorial','Création de contenu, campagnes & animation'],"Un lancement produit : une page web dédiée, des publications Instagram et une campagne de contenus pensée ensemble.",'Développer ma présence digitale')+service_panel('experience','Des gens. Un lieu.<br>Un moment qui reste.',"On transforme votre idée en expérience : le concept, l’espace, les invitations et les détails qui donnent envie de se rencontrer.",'muse-event',['Concept événementiel & scénographie','Lancements, rencontres B2B & activations','Invitations, signalétique, affichage & écrans'],"Un lancement culturel : une invitation, un décor et une signalétique qui racontent la même histoire.",'Créer un événement / une activation')+'</div></div><p class="service-footnote">Un besoin précis ou un projet à 360° : on construit le bon périmètre avec vous.</p></div></section>'
def service_content():
 from editorial_services import render_editorial_services
 return render_editorial_services(service_mark, icon)

def faq():
 entries=[('Peut-on travailler sur un seul besoin ?',"Oui. Une identité, un site, une campagne ou un événement peut être abordé séparément. Nous définissons ensemble le périmètre adapté."),('Que faut-il pour démarrer ?',"Quelques mots sur votre activité, votre besoin et votre calendrier suffisent pour ouvrir la discussion. Un brief plus précis se construit ensuite ensemble."),('Comment sont définis le budget et les délais ?',"Ils dépendent des livrables, du périmètre et des contraintes de production. Nous les précisons dans une proposition avant de lancer le projet."),('Les projets de cette présentation sont-ils réels ?',"Les marques présentées sont fictives. Leurs images ont été générées pour explorer la nouvelle direction du site. Les partenaires affichés proviennent du site existant et ne sont pas liés à ces concepts.")]
 return '<section class="faq section container"><div><h2>On en parle<br><em>simplement.</em></h2><p>Encore une question ?<br><a href="mailto:contact@magic360.tn">contact@magic360.tn</a></p></div><div class="faq-list">'+''.join(f'<details><summary>{q}{icon("plus")}</summary><p>{a}</p></details>' for q,a in entries)+'</div></section>'
def contact():
 return f'''<section class="contact section" id="contact"><div class="container contact-layout"><div class="contact-intro"><span class="contact-spark" aria-hidden="true">{icon('spark')}</span><h2>Et si on faisait<br><em>un peu de Magic ?</em></h2><p>Une idée bien précise ou juste un début de réflexion ? Racontez-nous ce que vous avez en tête.</p><div class="contact-direct"><a href="tel:+21696913500">+216 96 913 500 {icon('up')}</a><a href="mailto:contact@magic360.tn">contact@magic360.tn {icon('up')}</a></div><span class="contact-location">Tunis, Tunisie · Agence créative 360°</span></div><form class="project-brief"><h3>Racontez-nous votre idée.</h3><p class="brief-reassurance">Pas besoin d’un brief parfait pour commencer.</p><label for="brief-name">Votre nom <span>(requis)</span><input id="brief-name" name="name" autocomplete="name" required maxlength="100" placeholder="Comment vous appelez-vous ?"></label><label for="brief-need">Votre besoin<select id="brief-need" name="need"><option>Clarifier ma stratégie</option><option>Construire ma marque</option><option>Développer ma présence digitale</option><option>Créer un événement / une activation</option><option>Plusieurs besoins / à définir</option></select></label><label for="brief-message">Quelques mots sur votre idée <span>(requis)</span><textarea id="brief-message" name="message" required rows="3" maxlength="2000" placeholder="Ce que vous voulez créer, pour qui et pour quand…"></textarea></label><button class="button" type="submit"><span>Préparer mon message</span><span class="button-icon">{icon('up')}</span></button><p class="form-note">Un brouillon WhatsApp, à relire avant de l’envoyer.<br>Aucun message envoyé automatiquement.</p><div class="form-result" role="status" aria-live="polite"></div></form></div></section>'''
def build():
 write_sprite(ROOT)
 hero=f'''<section class="hero hero--impact"><div class="container hero-layout"><div class="hero-copy"><h1>De l’idée<br><em>à l’impact.</em></h1><p>Stratégie, branding, sites web, social media et événements. On donne du caractère à votre marque, puis on la fait vivre là où votre public vous rencontre.</p><div class="hero-actions"><a class="button hero-cta" href="#contact">Parlons de votre projet</a><a class="button hero-whatsapp" href="https://wa.me/21696913500" target="_blank" rel="noopener">{icon('whatsapp')}<span>WhatsApp</span></a></div></div>{wall()}</div></section>'''
 agency=f'''<section class="agency section" id="agence"><div class="container agency-layout"><div class="agency-visual"><div class="agency-image">{img('creative-table')}<div class="agency-image-caption"><span>Scène de création imaginée.<br>Image générée, à titre illustratif.</span></div></div><div class="agency-material">{img('naya-hands',sizes='(min-width:1000px) 260px, 160px')}</div><p class="agency-side-note">Les détails, ça se travaille.</p></div><div class="agency-copy"><h2>On commence<br>par <em>vous écouter.</em></h2><p>Ce que vous voulez raconter. Ce qui vous ressemble. Ce qui vous fait hésiter aussi. On en parle avant de passer aux premières idées.</p><p>Puis on cherche, on esquisse, on affine ensemble. La stratégie donne le cap ; les échanges font avancer la création.</p>{button('Faisons connaissance',cls='text-link')}</div></div></section>'''
 ribbon='<section class="explore section" id="realisations"><div class="container explore-heading"><h2>Et si on regardait<br><em>ça autrement ?</em></h2><div class="rail-controls"><button aria-label="Concept précédent" data-rail="previous">'+icon('left')+'</button><button aria-label="Concept suivant" data-rail="next">'+icon('arrow')+'</button></div></div><div class="explore-rail" tabindex="0" aria-label="Autres concepts créatifs">'+''.join(f'<article><button data-project="{dict(palma="palma-digital",muse="muse-event",grain="grain-strategy").get(key,key)}" aria-label="Explorer le concept {WORK[key]["title"]}"><span class="rail-image">{img(key,sizes="(min-width:900px) 35vw, 85vw")}<span class="concept-badge">Concept créatif</span></span><span class="rail-caption"><strong>{WORK[key]["title"]}</strong><span>{WORK[key]["label"]}</span>{icon("up")}</span></button></article>' for key in ['pulse','palma','muse','grain'])+'</div></section>'
 footer=f'''<footer class="footer"><div class="container"><div class="footer-top">{logo()}<p>Créativité, communication<br>et expériences de marque.</p><div><a href="#realisations">Les exemples</a><a href="#services">Nos expertises</a><a href="#solutions">Nos solutions</a><a href="#agence">L’agence</a></div><div><a href="mailto:contact@magic360.tn">contact@magic360.tn</a><a href="tel:+21696913500">+216 96 913 500</a><span>Tunis, Tunisie</span></div></div><div class="footer-bottom"><span>© 2026 Magic 360</span><span>Les idées n’attendent que vous.</span><a href="#top">Retour en haut {icon('up')}</a></div><details class="archives"><summary>Explorer les premières directions</summary><div><a href="/directions/studio/">Studio 360</a><a href="/directions/edition/">Édition</a><a href="/directions/cinema/">Grand écran</a><a href="/directions/atelier/">Atelier</a><a href="/directions/collectif/">Le Collectif</a></div></details><a class="editor-access" href="/admin/" hidden>Gérer les images</a></div></footer>'''
 dialog=f'''<dialog class="work-dialog" aria-labelledby="dialog-title"><div class="dialog-toolbar"><span>Exploration créative · concept fictif</span><button class="dialog-close" aria-label="Fermer le projet">{icon('close')}</button></div><div class="dialog-visual"></div><div class="dialog-album" role="group" aria-label="Images de cette marque"></div><div class="dialog-content"><div><h2 id="dialog-title"></h2><p class="dialog-category"></p></div><div><p class="dialog-description"></p><ul class="dialog-deliverables"></ul><p class="dialog-disclosure">Marque fictive et image générée pour cette présentation. Aucun lien avec les partenaires affichés ni résultat commercial associé.</p>{button('Imaginons votre projet',cls='text-link dialog-contact')}</div></div><div class="dialog-bottom"><button class="dialog-previous" aria-label="Projet précédent">{icon('left')}<span>Précédent</span></button><span class="dialog-position"></span><button class="dialog-next" aria-label="Projet suivant"><span>Suivant</span>{icon('arrow')}</button></div></dialog>'''
 header=f'''<header class="site-header"><div class="container nav-layout">{logo()}<span class="brand-description">Agence créative 360°<br>Tunis, Tunisie</span><nav class="main-nav" id="main-nav" aria-label="Navigation principale"><a href="#realisations">Les exemples</a><a href="#services">Nos expertises</a><a href="#solutions">Nos solutions</a><a href="#agence">L’agence</a></nav>{button('Parlons projet',cls='nav-cta')}<button class="menu-toggle" aria-controls="main-nav" aria-expanded="false" aria-label="Ouvrir le menu">{icon('menu')}</button></div></header>'''
 data=json.dumps(WORK,ensure_ascii=False).replace('</','<\\/')
 page=f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#102F29"><meta name="robots" content="noindex, follow"><title>Magic 360 — Des idées qui prennent vie | Agence créative en Tunisie</title><meta name="description" content="Branding, campagnes, digital et événementiel : Magic 360 réunit stratégie et création pour donner du caractère à votre marque en Tunisie."><link rel="canonical" href="https://magicbrandingco.com/"><meta property="og:title" content="Magic 360 — Des idées qui prennent vie"><meta property="og:description" content="Agence de communication et création à 360° en Tunisie."><meta property="og:image" content="https://magicbrandingco.com/assets/magic/naya-1400.webp"><meta property="og:type" content="website"><meta property="og:locale" content="fr_TN"><link rel="icon" href="/magiclogo.png"><link rel="preload" href="/assets/fonts/dm-sans-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="/assets/fonts/outfit-latin.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="/assets/fonts/magic-fonts.css"><link rel="stylesheet" href="/assets/magic.css"><script src="/assets/magic.js" defer></script><script id="work-data" type="application/json">{data}</script><script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","@id":"https://magicbrandingco.com/#organization","name":"Magic 360","url":"https://magicbrandingco.com/","logo":"https://magicbrandingco.com/magiclogo.png","telephone":"+21696913500","email":"contact@magic360.tn","address":{{"@type":"PostalAddress","addressLocality":"Tunis","addressCountry":"TN"}}}}</script></head>
<body id="top"><a class="skip-link" href="#main">Aller au contenu</a>{header}<main id="main">{hero}{partners()}{brand_story()}{service_content()}{agency}{ribbon}{faq()}{contact()}</main>{footer}{dialog}<noscript><p class="noscript-note">Pour préparer un brouillon ou explorer les galeries, activez JavaScript. Vous pouvez aussi nous joindre par téléphone ou par email.</p></noscript></body></html>'''
 page=page.replace('</head>', '<link rel="stylesheet" href="/assets/service-editorial.css"></head>')
 for asset in ['assets/magic.css','assets/magic.js','assets/fonts/magic-fonts.css','assets/service-editorial.css']:
  version=sha256((ROOT/asset).read_bytes()).hexdigest()[:12]
  page=page.replace(f'/{asset}"',f'/{asset}?v={version}"')
 from solution_variants import apply_solution, solution_sections, build_solution_variants
 preview_page=page
 page=apply_solution(page, solution_sections(icon)['editorial'])
 page=page.replace('content="noindex, follow"','content="index, follow"')
 temporary=ROOT/'index.html.tmp'
 temporary.write_text(page.replace('><','>\n<'),encoding='utf-8')
 temporary.replace(ROOT/'index.html')
 from service_variants import build_service_variants
 build_service_variants(page, service_content(), service_mark, img, icon)
 build_solution_variants(preview_page, icon)
 print('Built Magic in motion homepage. Original five directions preserved.')
if __name__=='__main__':build()
