document.addEventListener('DOMContentLoaded', () => {
    // Navbar Transition
    const navEl = document.querySelector('.nav');
    const navSect1El = document.querySelector('.section1');
    const navSect2El = document.querySelector('.section2');
    const navLinksEl = document.querySelector('.navLinks');
    const logoEl = document.querySelector('.navLogo');
    const logo2El = document.querySelector('.navLogo2');
    const navButtonsEl = document.querySelector('.navButtons');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY >= 20) {
            navEl.classList.add('navScrolled');
            navSect1El.classList.add('section1Scrolled');
            navSect2El.classList.add('section2Scrolled');
            navLinksEl.classList.add('navLinksScrolled');
            logoEl.classList.add('navLogoScrolled');
            navButtonsEl.classList.add('navButtonsScrolled');
    
            logo2El.setAttribute("style", "transform: translateY(0);");
        } else if (window.scrollY < 20) {
            navEl.classList.remove('navScrolled');
            navSect1El.classList.remove('section1Scrolled');
            navSect2El.classList.remove('section2Scrolled');
            navLinksEl.classList.remove('navLinksScrolled');
            logoEl.classList.remove('navLogoScrolled');
            navButtonsEl.classList.remove('navButtonsScrolled');
    
            logo2El.setAttribute("style", "transform: translateY(-100);");
        }
    })
});