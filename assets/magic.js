(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const editorLink=document.querySelector('.editor-access');
  if(editorLink){if(['localhost','127.0.0.1','[::1]'].includes(location.hostname))editorLink.hidden=false;else editorLink.remove();}
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const nav = document.querySelector('#main-nav');
  const menu = document.querySelector('.menu-toggle');
  const closeMenu = () => {menu.setAttribute('aria-expanded','false');menu.setAttribute('aria-label','Ouvrir le menu');nav.classList.remove('is-open');};
  menu.addEventListener('click', () => {const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));menu.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');nav.classList.toggle('is-open',open);});
  nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
  document.addEventListener('keydown', e=>{if(e.key==='Escape'&&menu.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus();}});

  const header=document.querySelector('.site-header');
  const hero=document.querySelector('.hero');
  const wall=document.querySelector('.campaign-wall');
  const control=document.querySelector('.motion-control');
  let explicitlyPaused=false;
  try {explicitlyPaused=sessionStorage.getItem('magic-motion-paused')==='true';} catch {}
  const syncMotion=()=>{wall.classList.toggle('is-paused',explicitlyPaused);control.setAttribute('aria-pressed',String(explicitlyPaused));control.setAttribute('aria-label',explicitlyPaused?'Reprendre le mouvement':'Mettre le mouvement en pause');control.querySelector('use').setAttribute('href',explicitlyPaused?'/assets/magic-icons.svg#magic-play-solid':'/assets/magic-icons.svg#magic-pause');};
  control.addEventListener('click',()=>{explicitlyPaused=!explicitlyPaused;try {sessionStorage.setItem('magic-motion-paused',String(explicitlyPaused));}catch{}syncMotion();});syncMotion();
  let wallVisible=true;
  const syncVisibility=()=>wall.classList.toggle('is-sleeping',document.hidden||!wallVisible);
  document.addEventListener('visibilitychange',syncVisibility);
  if('IntersectionObserver' in window){new IntersectionObserver(entries=>{wallVisible=entries[0].isIntersecting;syncVisibility();},{threshold:0}).observe(wall);}

  if('IntersectionObserver' in window){new IntersectionObserver(entries=>header.classList.toggle('is-scrolled',!entries[0].isIntersecting),{threshold:0}).observe(hero);}

  const partnerSection=document.querySelector('.partners--ribbons');
  if(partnerSection){
    let partnersVisible=true;
    const syncPartnerMotion=()=>{
      partnerSection.classList.toggle('is-sleeping',document.hidden||!partnersVisible);
    };
    document.addEventListener('visibilitychange',syncPartnerMotion);
    if('IntersectionObserver' in window)new IntersectionObserver(entries=>{
      partnersVisible=entries[0].isIntersecting;
      if(partnersVisible)partnerSection.querySelectorAll('img').forEach(image=>{image.loading='eager';});
      syncPartnerMotion();
    },{threshold:0}).observe(partnerSection);
    syncPartnerMotion();
  }

  const tabs=[...document.querySelectorAll('[role="tab"]')];
  const panels=[...document.querySelectorAll('.service-panel')];
  const activateTab=(tab,animate=true)=>{
    tabs.forEach(t=>{t.setAttribute('aria-selected',String(t===tab));t.tabIndex=t===tab?0:-1;});
    panels.forEach(panel=>{const active=panel.id===tab.getAttribute('aria-controls');panel.hidden=!active;if(active&&animate&&!motion.matches)panel.animate([{opacity:.5,clipPath:'inset(0 2% 0 0)'},{opacity:1,clipPath:'inset(0 0 0 0)'}],{duration:320,easing:'cubic-bezier(.16,1,.3,1)'});});
  };
  tabs.forEach((tab,i)=>{
    tab.addEventListener('click',()=>activateTab(tab));
    tab.addEventListener('keydown',e=>{let target;if(['ArrowDown','ArrowRight'].includes(e.key))target=tabs[(i+1)%tabs.length];if(['ArrowUp','ArrowLeft'].includes(e.key))target=tabs[(i-1+tabs.length)%tabs.length];if(e.key==='Home')target=tabs[0];if(e.key==='End')target=tabs.at(-1);if(target){e.preventDefault();activateTab(target);target.focus();}});
  });if(tabs.length)activateTab(tabs[0],false);
  panels.forEach(panel=>panel.querySelector('a').addEventListener('click',()=>{const select=document.querySelector('#brief-need');select.value=panel.dataset.need;select.dispatchEvent(new Event('input',{bubbles:true}));}));
  document.querySelectorAll('[data-service]').forEach(link=>link.addEventListener('click',()=>activateTab(document.getElementById(`tab-${link.dataset.service}`))));
  document.querySelectorAll('[data-service-need]').forEach(link=>link.addEventListener('click',()=>{
    const select=document.querySelector('#brief-need');select.value=link.dataset.serviceNeed;select.dispatchEvent(new Event('input',{bubbles:true}));
  }));

  const rail=document.querySelector('.explore-rail');
  document.querySelectorAll('[data-rail]').forEach(button=>button.addEventListener('click',()=>{
    const item=rail.querySelector('article');const gap=parseFloat(getComputedStyle(rail).gap)||18;
    rail.scrollBy({left:(item.getBoundingClientRect().width+gap)*(button.dataset.rail==='next'?1:-1),behavior:motion.matches?'instant':'smooth'});
  }));

  const work=JSON.parse(document.querySelector('#work-data').textContent);
  const keys=[...new Set([...document.querySelectorAll('[data-project]')].map(button=>button.dataset.project))];const dialog=document.querySelector('.work-dialog');let currentKey,currentImage=0,opener;
  const drawAsset=index=>{
    const images=work[currentKey].images;currentImage=(index+images.length)%images.length;const asset=images[currentImage];
    const image=new Image();image.alt=asset.alt;image.width=1536;image.height=1024;image.sizes='(min-width:1000px) 1050px, 100vw';image.srcset=`/assets/magic/${asset.key}-480.webp 480w, /assets/magic/${asset.key}-900.webp 900w, /assets/magic/${asset.key}-1400.webp 1400w`;image.src=`/assets/magic/${asset.key}-900.webp`;
    dialog.querySelector('.dialog-visual').replaceChildren(image);
    dialog.querySelectorAll('.dialog-album button').forEach((button,i)=>button.setAttribute('aria-pressed',String(i===currentImage)));
    dialog.querySelector('.dialog-position').textContent=`Image ${currentImage+1} / ${images.length} · Concept ${keys.indexOf(currentKey)+1} / ${keys.length}`;
  };
  const drawProject=(key,index=0)=>{
    currentKey=key;const data=work[key];
    const thumbnails=data.images.map((asset,i)=>{const button=document.createElement('button');button.type='button';button.setAttribute('aria-label',`Voir ${data.title}, image ${i+1} sur ${data.images.length}`);const thumb=new Image();thumb.src=`/assets/magic/${asset.key}-480.webp`;thumb.alt='';thumb.width=1536;thumb.height=1024;button.append(thumb);button.addEventListener('click',()=>drawAsset(i));return button;});
    dialog.querySelector('.dialog-album').replaceChildren(...thumbnails);
    drawAsset(index);dialog.querySelector('#dialog-title').textContent=data.title;dialog.querySelector('.dialog-category').textContent=data.label;dialog.querySelector('.dialog-description').textContent=data.description;
    dialog.querySelector('.dialog-deliverables').replaceChildren(...data.deliverables.map(text=>{const li=document.createElement('li');li.textContent=text;return li;}));
  };
  document.querySelectorAll('[data-project]').forEach(button=>button.addEventListener('click',()=>{
    opener=button;drawProject(button.dataset.project,Number(button.dataset.imageIndex)||0);dialog.showModal();dialog.scrollTop=0;wall.classList.add('is-sleeping');
  }));
  const nextProject=delta=>drawProject(keys[(keys.indexOf(currentKey)+delta+keys.length)%keys.length]);
  dialog.querySelector('.dialog-next').addEventListener('click',()=>nextProject(1));dialog.querySelector('.dialog-previous').addEventListener('click',()=>nextProject(-1));
  dialog.addEventListener('keydown',e=>{if(e.key==='ArrowRight'){e.preventDefault();drawAsset(currentImage+1);}if(e.key==='ArrowLeft'){e.preventDefault();drawAsset(currentImage-1);}});
  dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
  dialog.addEventListener('close',()=>{syncVisibility();opener?.focus({preventScroll:true});});
  dialog.querySelector('.dialog-contact').addEventListener('click',()=>{dialog.close();});

  const form=document.querySelector('.project-brief');

  form.addEventListener('input',e=>{
    if(typeof e.target.setCustomValidity==='function')e.target.setCustomValidity('');
    const result=form.querySelector('.form-result');
    if(result.querySelector('a')){const note=document.createElement('p');note.textContent='Le texte a changé. Préparez à nouveau le brouillon.';result.replaceChildren(note);result.classList.add('is-stale');}
  });
  form.addEventListener('submit',e=>{
    e.preventDefault();
    for(const [id,message] of [['brief-name','Indiquez votre nom pour préparer le message.'],['brief-message','Ajoutez quelques mots sur votre idée.']]){const field=document.getElementById(id);field.setCustomValidity(field.value.trim()?'':message);}
    if(!form.reportValidity())return;
    const data=new FormData(form);const message=`Bonjour Magic 360, je m’appelle ${String(data.get('name')).trim()}.\nMon besoin : ${data.get('need')}.\n\n${String(data.get('message')).trim()}`;
    const result=form.querySelector('.form-result');result.classList.remove('is-stale');const note=document.createElement('p');note.textContent='Votre brouillon est prêt. Vous pouvez le relire dans WhatsApp avant de l’envoyer.';
    const link=document.createElement('a');link.href=`https://wa.me/21696913500?text=${encodeURIComponent(message)}`;link.target='_blank';link.rel='noopener';link.textContent='Ouvrir mon brouillon WhatsApp';
    result.replaceChildren(note,link);link.focus();
  });
})();
