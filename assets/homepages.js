(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#main-nav');
  const closeMenu = () => {menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Ouvrir le menu');nav.classList.remove('is-open');};
  menu.addEventListener('click', () => {const open=menu.getAttribute('aria-expanded') !== 'true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');nav.classList.toggle('is-open',open);});
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
  document.addEventListener('keydown',e=>{if(e.key==='Escape' && menu.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus();}});
  document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{
    const area=button.closest('.gallery-area'); let count=0;
    area.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
    area.querySelectorAll('[data-category]').forEach(card=>{card.hidden=button.dataset.filter!=='all' && card.dataset.category!==button.dataset.filter;if(!card.hidden)count++;});
    area.querySelector('.filter-status').textContent=`${count} concept${count>1?'s':''} affiché${count>1?'s':''}.`;
  }));
  const descriptions={packaging:'Une piste de marque pour une huile d’olive : identité, étiquette, coffret et direction photographique.',campaign:'Une campagne culturelle imaginée pour vivre dans la rue, sur les écrans et dans les conversations.',event:'Une proposition de scénographie pour réunir un public autour d’une marque.',hospitality:'Un univers hôtelier fictif décliné en papeterie, menu et objets de bienvenue.',digital:'Un concept de lancement qui relie packaging, visuels produits et contenus pour les réseaux sociaux.'};
  const dialog=document.querySelector('.project-dialog'); let opener;
  document.querySelectorAll('[data-project]').forEach(button=>button.addEventListener('click',()=>{
    opener=button;const img=button.querySelector('img').cloneNode();img.loading='eager';img.sizes='(min-width: 900px) 900px, 100vw';
    dialog.querySelector('.dialog-image').replaceChildren(img);
    dialog.querySelector('#project-title').textContent=button.querySelector('strong').textContent;
    dialog.querySelector('.dialog-category').textContent=button.querySelector('.project-caption span span').textContent;
    dialog.querySelector('.dialog-description').textContent=descriptions[button.dataset.project];
    dialog.showModal(); document.body.classList.add('dialog-open');
  }));
  dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
  dialog.addEventListener('close',()=>{document.body.classList.remove('dialog-open');opener?.focus();});
  dialog.querySelector('.dialog-contact').addEventListener('click',()=>{dialog.close();document.querySelector('#brief-name').focus({preventScroll:true});});
  document.querySelectorAll('[data-service]').forEach(a=>a.addEventListener('click',()=>{const select=document.querySelector('#brief-service');const option=Array.from(select.options).find(o=>o.textContent===a.dataset.service);if(option)select.value=option.value;}));
  document.querySelectorAll('.material-card').forEach(a=>a.addEventListener('click',()=>{const detail=document.querySelector(a.getAttribute('href'));detail.open=true;}));
  document.querySelector('.brief-form').addEventListener('submit',e=>{
    e.preventDefault();const form=e.currentTarget;if(!form.reportValidity())return;
    const data=new FormData(form);const message=`Bonjour Magic 360, je m’appelle ${data.get('name')}.\nMon besoin : ${data.get('service')}.\n\n${data.get('message')}`;
    const url=`https://wa.me/21696913500?text=${encodeURIComponent(message)}`;
    const status=form.querySelector('.form-status');status.replaceChildren();
    const link=document.createElement('a');link.href=url;link.target='_blank';link.rel='noopener';link.textContent='Ouvrir mon brouillon WhatsApp ↗';
    status.append('Brouillon prêt. Aucun message envoyé. ',link);link.focus();
  });
})();
