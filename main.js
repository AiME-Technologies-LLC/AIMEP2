document.addEventListener('DOMContentLoaded', () => {
    // Cursor
    const cursor = document.querySelector('.cursor');
    document.addEventListener('mousemove', e => {
        cursor.setAttribute("style", "top: " + e.pageY + "px; left: " + e.pageX + "px;")
    })
    
    // Navbar Transition
    const navEl = document.querySelector('.navbar');
    const navSect1El = document.querySelector('.section1');
    const navSect2El = document.querySelector('.section2');
    const navLinksEl = document.querySelector('.navLinks');
    const logoEl = document.querySelector('.navLogo');
    const logo2El = document.querySelector('.navLogo2');
    const loginEl = document.querySelector('.login');

    window.addEventListener('scroll', () => {
        if (window.scrollY >= 10) {
            navEl.classList.add('navbarScrolled');
            navSect1El.classList.add('section1Scrolled');
            navSect2El.classList.add('section2Scrolled');
            navLinksEl.classList.add('navLinksScrolled');
            logoEl.classList.add('navLogoScrolled');
            loginEl.classList.add('loginScrolled');

            logo2El.setAttribute("style", "transform: translateY(0);");
        } else if (window.scrollY < 10) {
            navEl.classList.remove('navbarScrolled');
            navSect1El.classList.remove('section1Scrolled');
            navSect2El.classList.remove('section2Scrolled');
            navLinksEl.classList.remove('navLinksScrolled');
            logoEl.classList.remove('navLogoScrolled');
            loginEl.classList.remove('loginScrolled');

            logo2El.setAttribute("style", "transform: translateY(-100);");
        }
    })
});
