






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