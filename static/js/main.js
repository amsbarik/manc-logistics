
////////////////////////////////////////////////////
// header mobile menu toggle js start 

const menuBtn = document.getElementById('menuBtn');
const closeBtn = document.getElementById('closeMenu');
const mobileMenu = document.getElementById('mobileMenu');
const overlay = document.getElementById('mobileOverlay');
const navLinks = document.querySelectorAll('.mobile-link');

function openMenu() {
    overlay.classList.remove(
        'opacity-0',
        'invisible'
    );

    mobileMenu.classList.remove(
        '-translate-x-full'
    );
}

function closeMenu() {

    mobileMenu.classList.add(
        '-translate-x-full'
    );

    overlay.classList.add(
        'opacity-0'
    );

    setTimeout(() => {

        overlay.classList.add(
            'invisible'
        );

    },300);
}

menuBtn.addEventListener(
    'click',
    openMenu
);

closeBtn.addEventListener(
    'click',
    closeMenu
);

navLinks.forEach(link => {

    link.addEventListener(
        'click',
        closeMenu
    );

});

overlay.addEventListener(
    'click',
    (e) => {

        if(e.target === overlay){

            closeMenu();

        }

    }
);


// header mobile menu toggle js end




/////////////////////////////////////
// index page js start 
///////////////// Hero Slider Js start


const slides = document.querySelectorAll(".slide");
const indicators = document.querySelectorAll(".indicator");

let currentSlide = 0;

// ================= SHOW SLIDE =================

function showSlide(index) {

    slides.forEach((slide, i) => {

        slide.classList.remove("active-slide");

        indicators[i].classList.remove(
            "w-10",
            "bg-white"
        );

        indicators[i].classList.add(
            "w-2",
            "bg-white/40"
        );

    });

    slides[index].classList.add("active-slide");

    indicators[index].classList.remove(
        "w-2",
        "bg-white/40"
    );

    indicators[index].classList.add(
        "w-10",
        "bg-white"
    );

    currentSlide = index;
}

// ================= NEXT SLIDE =================

function nextSlide() {

    currentSlide++;

    if(currentSlide >= slides.length){
        currentSlide = 0;
    }

    showSlide(currentSlide);
}

// ================= PREV SLIDE =================

function prevSlide() {

    currentSlide--;

    if(currentSlide < 0){
        currentSlide = slides.length - 1;
    }

    showSlide(currentSlide);
}

// ================= BUTTON EVENTS =================

document
    .getElementById("nextBtn")
    .addEventListener("click", nextSlide);

document
    .getElementById("prevBtn")
    .addEventListener("click", prevSlide);

// ================= INDICATOR EVENTS =================

indicators.forEach((indicator, index) => {

    indicator.addEventListener("click", () => {

        showSlide(index);

    });

});

// ================= AUTO PLAY =================

setInterval(() => {

    nextSlide();

}, 5000);

// ================= INITIAL =================

showSlide(0);


///////////////// Hero Slider Js end




////////////////////////////////////////////////////////////
// FAQ js start 

const faqItems=document.querySelectorAll('.faq-item');

function openItem(item){

    const content=item.querySelector('.faq-content');
    const plus=item.querySelector('.icon-plus');
    const minus=item.querySelector('.icon-minus');
    const icon=item.querySelector('.icon-wrap');
    const question=item.querySelector('.faq-question');

    item.classList.add('active');

    content.style.height=content.scrollHeight+'px';
    content.classList.remove('opacity-0');
    content.classList.add('opacity-100');

    plus.classList.add('hidden');
    minus.classList.remove('hidden');

    // icon.classList.add('rotate-180');

    question.classList.add('text-primary');

}

function closeItem(item){

    const content=item.querySelector('.faq-content');
    const plus=item.querySelector('.icon-plus');
    const minus=item.querySelector('.icon-minus');
    const icon=item.querySelector('.icon-wrap');
    const question=item.querySelector('.faq-question');

    item.classList.remove('active');

    content.style.height='0px';
    content.classList.remove('opacity-100');
    content.classList.add('opacity-0');

    plus.classList.remove('hidden');
    minus.classList.add('hidden');

    // icon.classList.remove('rotate-180'); 

    question.classList.remove('text-primary');

}


window.addEventListener('load',()=>{

    const first=document.querySelector('.faq-item.active');

    openItem(first);

});


faqItems.forEach(item=>{

    item.querySelector('.faq-btn')
    .addEventListener('click',()=>{

        const isActive=item.classList.contains('active');

        faqItems.forEach(faq=>{

            if(faq!==item){

            closeItem(faq);

            }

        });

        if(isActive){

            closeItem(item);

        }else{

            openItem(item);

        }

    });

});


// FAQ js end 
///////////////////////////////////////////////////////



/////////////////////////////////////////////////////////////////////////////

// partners slider js start /////////////////////////////////
(function () {
  const track = document.getElementById('partnersTrack');
  const slider = document.getElementById('partnersSlider');
  if (!track || !slider) return;

  function duplicateOnce() {
    if (track.dataset.duplicated === 'true') return;
    track.innerHTML += track.innerHTML;
    track.dataset.duplicated = 'true';
  }

  function imagesLoaded(parent, cb) {
    const imgs = parent.querySelectorAll('img');
    let total = imgs.length, loaded = 0;
    if (!total) return cb();
    imgs.forEach(img => {
      if (img.complete && img.naturalWidth !== 0) {
        loaded++;
        if (loaded === total) cb();
      } else {
        img.addEventListener('load', () => { loaded++; if (loaded === total) cb(); });
        img.addEventListener('error', () => { loaded++; if (loaded === total) cb(); });
      }
    });
  }

  let pos = 0, trackWidth = 0, lastTime = 0;
  let isDragging = false, pointerId = null, startX = 0, startPos = 0;
  let momentum = 0, hoverPaused = false;

  const style = getComputedStyle(document.documentElement);
  const AUTO_SPEED = parseFloat(style.getPropertyValue('--auto-speed')) || 0.035;

  function normalizePos() {
    if (!trackWidth) return;
    while (pos <= -trackWidth) pos += trackWidth;
    while (pos > 0) pos -= trackWidth;
  }

  function updateTransform() {
    track.style.transform = `translate3d(${pos}px,0,0)`;
  }

  function rafLoop(now) {
    if (!lastTime) lastTime = now;
    const dt = Math.min(40, now - lastTime);
    lastTime = now;

    if (!isDragging && !hoverPaused) {
      if (Math.abs(momentum) > parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--min-momentum') || 0.001)) {
        pos += momentum * dt;
        const decayPerMs = 0.9985;
        momentum *= Math.pow(decayPerMs, dt);
        if (Math.abs(momentum) < 0.0005) momentum = 0;
      } else {
        pos -= AUTO_SPEED * dt;
      }
    }

    normalizePos();
    updateTransform();
    requestAnimationFrame(rafLoop);
  }

  function onPointerDown(e) {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    try { e.target.setPointerCapture(e.pointerId); } catch (err) { }
    isDragging = true; pointerId = e.pointerId;
    startX = e.clientX; startPos = pos; momentum = 0;
    slider.classList.add('dragging'); e.preventDefault();
  }

  function onPointerMove(e) {
    if (!isDragging || e.pointerId !== pointerId) return;
    const dx = e.clientX - startX; pos = startPos + dx;
    normalizePos(); updateTransform();
    const now = performance.now();
    if (!onPointerMove._lastTime) { onPointerMove._lastTime = now; onPointerMove._lastX = e.clientX; return; }
    const dt = now - onPointerMove._lastTime;
    if (dt > 0) {
      const vx = (e.clientX - onPointerMove._lastX) / dt;
      momentum = vx * 0.9 + momentum * 0.1;
      onPointerMove._lastTime = now; onPointerMove._lastX = e.clientX;
    }
  }

  function endDrag(e) {
    if (!isDragging) return;
    try { e.target.releasePointerCapture(e.pointerId); } catch (err) { }
    isDragging = false; pointerId = null; slider.classList.remove('dragging');
    if (Math.abs(momentum) < 0.0005) momentum = 0;
  }

  slider.addEventListener('mouseenter', () => { hoverPaused = true; });
  slider.addEventListener('mouseleave', () => { hoverPaused = false; });
  slider.addEventListener('pointerdown', onPointerDown, { passive: false });
  window.addEventListener('pointermove', onPointerMove, { passive: false });
  window.addEventListener('pointerup', endDrag, { passive: true });
  window.addEventListener('pointercancel', endDrag, { passive: true });

  function recompute() {
    trackWidth = track.scrollWidth / 2 || 0;
    normalizePos(); updateTransform();
  }
  window.addEventListener('resize', () => { setTimeout(recompute, 50); });

  function initOnce() {
    duplicateOnce();
    imagesLoaded(track, () => {
      recompute(); normalizePos(); lastTime = 0;
      requestAnimationFrame(rafLoop);
    });
  }

  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    initOnce();
  } else {
    window.addEventListener('DOMContentLoaded', initOnce);
  }
})();

// partners slider js end///////////////////////////////









/////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////
// Nav & Tab Js start /////

const tabs=document.querySelectorAll('.tab-btn');
const contents=document.querySelectorAll('.tab-content');
const container=document.getElementById('tab-container');


function resetTabs(){

    tabs.forEach(tab=>{

        tab.classList.remove(
            'bg-primary',
            'border',
            'border-primary',
            'text-white'
        );

        tab.classList.add(
            'bg-white',
            'text-dark',
            'border',
            'border-primary'
        );

    });



    contents.forEach(content=>{

        content.classList.remove(
            'opacity-100',
            'translate-y-0'
        );

        content.classList.add(
            'opacity-0',
            'translate-y-10',
            'pointer-events-none'
        );

    });

}



tabs.forEach(tab=>{

    tab.addEventListener('click',()=>{

        resetTabs();



        tab.classList.remove(
            'bg-white',
            'text-dark'
        );

        tab.classList.add(
            'bg-primary',
            'border',
            'border-primary',
            'text-white'
        );



        const target=document.getElementById(tab.dataset.tab);



        setTimeout(()=>{

            target.classList.remove(
                'opacity-0',
                'translate-y-10',
                'pointer-events-none'
            );

            target.classList.add(
                'opacity-100',
                'translate-y-0'
            );



            container.style.height=
            target.scrollHeight+'px';



        },200);

    });

});




/* Default Active */

tabs[0].click();




// Nav & Tab Js end
//////////////////////////////////////////////////////////////////////////////////





////////////////////////////////////////////////////////////////////////////////////
// scroll progress + back-to-top button js start 
const scrollBtn = document.getElementById("scrollBtn");
const progressCircle = document.getElementById("progressCircle");
const topBtn = document.getElementById("topBtn");

const radius = 42;
const circumference = 2 * Math.PI * radius;

progressCircle.style.strokeDasharray = circumference;

window.addEventListener("scroll", () => {

    const scrollTop = window.scrollY;

    const docHeight =
        document.documentElement.scrollHeight -
        document.documentElement.clientHeight;

    const progress = scrollTop / docHeight;

    const offset = circumference - progress * circumference;

    progressCircle.style.strokeDashoffset = offset;

    // show after scrolling down
    if(scrollTop > 300){

        scrollBtn.classList.remove(
            "opacity-0",
            "invisible"
        );

        scrollBtn.classList.add(
            "opacity-100",
            "visible"
        );

    } else {

        scrollBtn.classList.add(
            "opacity-0",
            "invisible"
        );

        scrollBtn.classList.remove(
            "opacity-100",
            "visible"
        );
    }

});

topBtn.addEventListener("click", ()=>{

    window.scrollTo({
        top:0,
        behavior:"smooth"
    });

});

// scroll progress + back-to-top button js end
//////////////////////////////////////////////////////////////////////////////