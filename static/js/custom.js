document.addEventListener('DOMContentLoaded', function () {
    const pathname = window.location.pathname;
    const navbarTitle = document.getElementById('navbar-title');
    const navbarSubtitle = document.getElementById('navbar-subtitle');
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    navbarSubtitle.style.opacity = 0;
    navbarSubtitle.style.transition = 'opacity 0.5s ease-in-out';

    function removeActiveClass() {
        navLinks.forEach(link => {
            link.classList.remove('nav-active');
        });
    }

    function setActiveNavLink() {
        let section = 'home';
        if (pathname.includes('services')) {
            section = 'services';
        } else if (pathname.includes('blog')) {
            section = 'blog';
        } else if (pathname.includes('appointments')) {
            section = 'appointments';
        }

        removeActiveClass();
        const activeLink = document.querySelector(`.navbar-nav .nav-link[data-section="${section}"]`);
        if (activeLink) {
            activeLink.classList.add('nav-active');
        }
    }

    if (pathname === "/" || pathname.includes('home')) {
        navbarTitle.textContent = 'Home';
        navbarSubtitle.textContent = 'Welcome to my site';
    } else if (pathname.includes('services')) {
        navbarTitle.textContent = 'Services';
        navbarSubtitle.textContent = 'What we offer';
    } else if (pathname.includes('blog')) {
        navbarTitle.textContent = 'Blog';
        navbarSubtitle.textContent = 'Latest news';
    }

    setActiveNavLink();

    setTimeout(() => {
        navbarSubtitle.style.opacity = 1;
    }, 500);
});

