






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