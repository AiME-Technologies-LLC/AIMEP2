document.addEventListener('DOMContentLoaded', () => {
    // Cursor
    const cursor = document.querySelector('.cursor');
    document.addEventListener('mousemove', e => {
        cursor.setAttribute("style", "top: " + e.pageY + "px; left: " + e.pageX + "px;")
    })

    // Navbar Transition
    const navEl = document.querySelector('.navBar');

    window.addEventListener('scroll', () => {
        if (window.scrollY >= 2) {
            navEl.classList.add('navBarScrolled');
        } else if (window.scrollY < 2) {
            navEl.classList.remove('navBarScrolled');
        }
    })

    // Our Product: Carousel
    const slds = document.getElementById('slds');
    const prevButton = document.querySelector('.carousel-button.prev');
    const nextButton = document.querySelector('.carousel-button.next');
    const totalImages = slds.children.length;
    let currentIndex = 0;

    const updateCarousel = () => {
        const sldWidth = slds.querySelector('img').clientWidth;
        slds.style.transform = `translateX(-${sldWidth * currentIndex}px)`;
    };

    prevButton.addEventListener('click', () => {
        if (currentIndex > 0) {
            currentIndex--;
            updateCarousel();
        }
    });

    nextButton.addEventListener('click', () => {
        if (currentIndex < totalImages - 1) {
            currentIndex++;
            updateCarousel();
        }
    });
});
