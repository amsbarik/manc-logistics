






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