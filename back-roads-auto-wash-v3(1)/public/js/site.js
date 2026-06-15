(function(){
  var btn=document.getElementById('hamburger'), links=document.getElementById('navLinks');
  if(btn&&links){
    btn.addEventListener('click',function(){
      var open=links.classList.toggle('open');
      btn.setAttribute('aria-expanded',open?'true':'false');
    });
    links.addEventListener('click',function(e){
      if(e.target.tagName==='A'){links.classList.remove('open');btn.setAttribute('aria-expanded','false');}
    });
  }
})();
(function(){
  var els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('in-view')});return;}
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in-view');io.unobserve(en.target);}});
  },{threshold:.12,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(el){io.observe(el)});
})();
(function(){
  var form=document.getElementById('bookForm'); if(!form) return;
  var thanks=document.getElementById('thankyou');
  form.addEventListener('submit',function(e){
    e.preventDefault();
    var checks=form.querySelectorAll('input[name="services"]:checked');
    if(checks.length===0){alert('Please select at least one service.');return;}
    if(!form.checkValidity()){form.reportValidity();return;}
    form.style.display='none';
    if(thanks){thanks.style.display='block';thanks.scrollIntoView({behavior:'smooth',block:'center'});}
  });
})();
