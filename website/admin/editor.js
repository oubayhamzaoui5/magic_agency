(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);
  const clone = value => JSON.parse(JSON.stringify(value));
  const sideName = lane => ['gauche','centre','droite'][lane];
  let state, saved, selection = null, dragging = null, busy = false;
  const icon = name => {const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');svg.setAttribute('viewBox','0 0 32 32');svg.setAttribute('aria-hidden','true');const use=document.createElementNS(svg.namespaceURI,'use');use.setAttribute('href',`/assets/magic-icons.svg#magic-${name}`);svg.append(use);return svg;};
  const element = (tag, className, text) => {const el=document.createElement(tag);if(className)el.className=className;if(text!==undefined)el.textContent=text;return el;};
  const dirty = () => state && JSON.stringify(state.content)!==JSON.stringify(saved);
  function sync(message) {
    const changed=dirty();
    $('#save').disabled=!changed||busy;$('#discard').disabled=!changed||busy;
    $('#save').textContent=busy?'Enregistrement…':'Enregistrer';
    $('#save-status').textContent=message || (changed?'Modifications non enregistrées.':'Aucune modification.');
  }
  function loginView(message='') {
    state=null;saved=null;selection=null;busy=false;
    $('#loading').hidden=true;$('#editor').hidden=true;$('#logout').hidden=true;$('#login').hidden=false;
    $('#login-error').textContent=message;
  }
  async function request(url, options={}) {
    const headers={...(options.headers||{})};
    if(options.method==='POST'&&url!=='/api/login')headers['X-CSRF-Token']=state?.csrf||'';
    const response=await fetch(url,{...options,headers,credentials:'same-origin',cache:'no-store'});
    let result;try{result=await response.json();}catch{throw new Error('Le serveur ne répond pas. Vérifiez qu’il est démarré.');}
    if(!response.ok){if(response.status===401&&url!=='/api/login')loginView('Votre session a expiré. Reconnectez-vous.');throw new Error(result.error||'Action impossible. Réessayez.');}
    return result;
  }
  async function load() {
    try {
      state=await request('/api/admin/state');saved=clone(state.content);
      $('#loading').hidden=true;$('#login').hidden=true;$('#editor').hidden=false;$('#logout').hidden=false;
      $('#editor-error').textContent='';renderLanes();renderLibrary();sync();
    } catch(error){if(!state)loginView(error.message);else $('#editor-error').textContent=error.message;}
  }
  $('#login-form').addEventListener('submit',async event=>{
    event.preventDefault();const button=event.submitter;button.disabled=true;button.textContent='Connexion…';$('#login-error').textContent='';
    try{await request('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({password:$('#password').value})});$('#password').value='';await load();}
    catch(error){$('#login-error').textContent=error.message;}
    finally{button.disabled=false;button.textContent='Se connecter';}
  });
  $('#show-password').addEventListener('click',()=>{const input=$('#password'),show=input.type==='password';input.type=show?'text':'password';$('#show-password').textContent=show?'Masquer':'Afficher';$('#show-password').setAttribute('aria-label',show?'Masquer le mot de passe':'Afficher le mot de passe');$('#show-password').setAttribute('aria-pressed',String(show));});
  $('#logout').addEventListener('click',async()=>{
    if(dirty()&&!confirm('Quitter sans enregistrer vos modifications ?'))return;
    try{await request('/api/logout',{method:'POST'});loginView();$('#password').focus();}catch(error){$('#editor-error').textContent=error.message;}
  });
  function chooseTarget(lane,index=null) {
    selection={lane,index};renderLanes();renderLibrary();$('#close-library').hidden=false;
    $('#selection-help').textContent=index===null?`Choisissez une image à ajouter à la colonne ${sideName(lane)}.`:`Choisissez l’image qui remplacera « ${state.content.lanes[lane][index].label || 'Sans nom'} ».`;
    if(matchMedia('(max-width:800px)').matches)$('#library-panel').scrollIntoView({behavior:'instant',block:'start'});
    $('#search').focus({preventScroll:true});
  }
  function clearSelection() {selection=null;$('#close-library').hidden=true;$('#selection-help').textContent='Choisissez « Ajouter » ou « Remplacer » dans une colonne.';renderLanes();renderLibrary();}
  $('#close-library').addEventListener('click',clearSelection);
  function applyImage(asset) {
    if(!selection)return;
    const {lane,index}=selection;
    if(index===null){if(state.content.lanes[lane].length>=12)return;state.content.lanes[lane].push({image:asset.id,label:asset.label});}
    else state.content.lanes[lane][index].image=asset.id;
    const newIndex=index===null?state.content.lanes[lane].length-1:index;
    clearSelection();sync('Image sélectionnée. Enregistrez pour l’afficher sur le site.');
    const tile=$(`#lanes [data-lane="${lane}"][data-index="${newIndex}"]`);
    if(matchMedia('(max-width:800px)').matches)tile.scrollIntoView({behavior:'instant',block:'center'});
    tile.querySelector('input').focus({preventScroll:true});
  }
  function action(label,name,onClick,className='',disabled=false) {
    const button=element('button',className);button.type='button';button.setAttribute('aria-label',label);button.title=label;button.append(icon(name));button.disabled=disabled;button.addEventListener('click',onClick);return button;
  }
  function move(fromLane,index,toLane,toIndex) {
    if(fromLane!==toLane&&state.content.lanes[toLane].length>=12)return;
    if(fromLane!==toLane&&state.content.lanes[fromLane].length===1)return;
    const [item]=state.content.lanes[fromLane].splice(index,1);state.content.lanes[toLane].splice(toIndex,0,item);
    selection=null;$('#close-library').hidden=true;renderLanes();renderLibrary();sync();
    $(`#lanes [data-lane="${toLane}"][data-index="${toIndex}"] input`).focus({preventScroll:true});
  }
  function renderLanes() {
    const fragment=document.createDocumentFragment();
    state.content.lanes.forEach((items,lane)=>{
      const section=element('section','lane'),heading=element('div','lane-heading'),title=element('h2','',`Colonne ${sideName(lane)}`);
      title.append(element('span','',`${items.length}/12`));
      const add=element('button','');add.append(icon('plus'),document.createTextNode('Ajouter'));add.disabled=items.length>=12;add.setAttribute('aria-label',`Ajouter une image : colonne ${sideName(lane)}`);add.addEventListener('click',()=>chooseTarget(lane));heading.append(title,add);
      const list=element('div','tile-list');
      items.forEach((item,index)=>{
        const asset=state.library.find(asset=>asset.id===item.image);
        const tile=element('article','tile');tile.dataset.lane=lane;tile.dataset.index=index;tile.draggable=true;
        if(selection?.lane===lane&&selection.index===index)tile.classList.add('is-target');
        const imageWrap=element('div','tile-image'),image=element('img');image.src=asset.src;image.alt=item.label||'Image du hero';image.loading='lazy';image.draggable=false;
        const replace=element('button','','Remplacer');replace.setAttribute('aria-label',`Remplacer ${item.label||'cette image'}`);replace.addEventListener('click',()=>chooseTarget(lane,index));imageWrap.append(image,replace);
        const body=element('div','tile-body'),label=element('label','',`Nom de l’image ${index+1}`),input=element('input');input.id=`label-${lane}-${index}`;input.value=item.label;input.maxLength=80;label.htmlFor=input.id;input.addEventListener('input',()=>{item.label=input.value;sync();});input.addEventListener('focus',()=>{tile.draggable=false;});input.addEventListener('blur',()=>{tile.draggable=true;});
        const controls=element('div','tile-controls');
        controls.append(action(`Monter ${item.label}`,'left',()=>move(lane,index,lane,index-1),'up',index===0),action(`Descendre ${item.label}`,'left',()=>move(lane,index,lane,index+1),'down',index===items.length-1));
        state.content.lanes.forEach((target,toLane)=>{if(toLane!==lane)controls.append(action(`Déplacer ${item.label} : colonne ${sideName(toLane)}`,'arrow',()=>move(lane,index,toLane,target.length),toLane<lane?'move-left':'',items.length===1||target.length>=12));});
        controls.append(action(`Retirer ${item.label}`,'close',()=>{items.splice(index,1);clearSelection();sync();},'remove',items.length===1));
        body.append(label,input,controls);tile.append(imageWrap,body);
        tile.addEventListener('dragstart',event=>{dragging={lane,index};event.dataTransfer.effectAllowed='move';event.dataTransfer.setData('text/plain',`${lane}:${index}`);tile.classList.add('dragging');});
        tile.addEventListener('dragend',()=>{dragging=null;document.querySelectorAll('.dragging,.drop-target').forEach(el=>el.classList.remove('dragging','drop-target'));});
        tile.addEventListener('dragover',event=>{if(dragging){event.preventDefault();tile.classList.add('drop-target');}});tile.addEventListener('dragleave',()=>tile.classList.remove('drop-target'));
        tile.addEventListener('drop',event=>{event.preventDefault();tile.classList.remove('drop-target');if(dragging){const from=dragging;dragging=null;if(from.lane!==lane||from.index!==index)move(from.lane,from.index,lane,index);}});
        list.append(tile);
      });
      section.append(heading,list);fragment.append(section);
    });
    $('#lanes').replaceChildren(fragment);
  }
  function renderLibrary() {
    const query=$('#search').value.toLocaleLowerCase('fr'),fragment=document.createDocumentFragment();
    const matches=state.library.filter(item=>(item.label+' '+item.id).toLocaleLowerCase('fr').includes(query));
    matches.forEach(item=>{const button=element('button'),image=element('img');image.src=item.src;image.alt='';image.loading='lazy';button.append(image,element('span','',item.label));button.disabled=!selection;button.setAttribute('aria-label',`Choisir ${item.label}`);button.addEventListener('click',()=>applyImage(item));fragment.append(button);});
    $('#library').replaceChildren(fragment);$('#library-status').textContent=matches.length?`${matches.length} images disponibles.`:'Aucune image trouvée. Essayez un autre nom ou importez une image.';
  }
  $('#search').addEventListener('input',()=>{if(state)renderLibrary();});
  $('#upload').addEventListener('change',async event=>{
    const file=event.target.files[0];if(!file)return;
    if(file.size>10*1024*1024){$('#editor-error').textContent='Cette image dépasse 10 Mo. Choisissez un fichier plus léger.';event.target.value='';return;}
    const input=event.target;input.disabled=true;$('#library-status').textContent='Importation en cours…';$('#editor-error').textContent='';
    try{const result=await request('/api/admin/upload',{method:'POST',headers:{'Content-Type':'application/octet-stream'},body:file});result.image.label=file.name.replace(/\.[^.]+$/,'').slice(0,80);state.library.unshift(result.image);$('#search').value='';renderLibrary();if(selection)applyImage(result.image);else $('#library-status').textContent='Image importée. Choisissez « Ajouter » ou « Remplacer » pour l’utiliser.';}
    catch(error){$('#editor-error').textContent=error.message;}
    finally{input.disabled=false;input.value='';}
  });
  $('#discard').addEventListener('click',()=>{state.content=clone(saved);clearSelection();$('#editor-error').textContent='';sync('Modifications annulées.');});
  $('#save').addEventListener('click',async()=>{
    busy=true;sync();$('#editor-error').textContent='';const submitted=clone(state.content);
    try{const result=await request('/api/admin/hero',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({content:submitted,revision:state.revision})});state.revision=result.revision;saved=submitted;sync(dirty()?'Enregistré. D’autres modifications restent à enregistrer.':'Enregistré. Rechargez le site pour voir vos images.');}
    catch(error){if(state)$('#editor-error').textContent=error.message;}
    finally{busy=false;if(state){$('#save').disabled=!dirty();$('#discard').disabled=!dirty();$('#save').textContent='Enregistrer';}}
  });
  window.addEventListener('beforeunload',event=>{if(dirty()){event.preventDefault();event.returnValue='';}});
  load();
})();
