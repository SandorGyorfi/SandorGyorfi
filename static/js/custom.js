document.addEventListener('DOMContentLoaded', function () {
    const sectionTitles = document.querySelectorAll('h2, h3');
    const navbarTitle = document.getElementById('navbar-title');
    const navbarSubtitle = document.getElementById('navbar-subtitle');
    let currentTitleIndex = 0;

    function cycleSectionTitles() {
        if (sectionTitles.length > 0) {
            navbarSubtitle.style.opacity = 0;
            setTimeout(function () {
                navbarSubtitle.textContent = sectionTitles[currentTitleIndex].textContent;
                navbarSubtitle.style.opacity = 1;
                currentTitleIndex = (currentTitleIndex + 1) % sectionTitles.length;
            }, 500);
        }
    }

    cycleSectionTitles();
    setInterval(cycleSectionTitles, 4000);

    const pathname = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

    function setActiveNavLink() {
        let section = 'home';
        if (pathname.includes('services')) {
            section = 'services';
            navbarTitle.textContent = 'Services';
        } else if (pathname.includes('blog')) {
            section = 'blog';
            navbarTitle.textContent = 'Blog';
        } else if (pathname.includes('appointments')) {
            section = 'appointments';
            navbarTitle.textContent = 'Appointments';
        } else {
            navbarTitle.textContent = 'Home';
        }

        navLinks.forEach(link => {
            link.classList.remove('nav-active');
            if (link.getAttribute('href').includes(section)) {
                link.classList.add('nav-active');
            }
        });
    }

    setActiveNavLink();
});

document.getElementById('shareBtn').addEventListener('click', async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title: '{{ blogpost.title }}',
          url: '{{ request.build_absolute_uri }}'
        });
        console.log('Content shared successfully');
      } catch (err) {
        console.error('Error sharing:', err);
      }
    } else {
      document.getElementById('fallbackShare').style.display = 'block';
    }
  });

  document.getElementById('copyBtn').addEventListener('click', () => {
    navigator.clipboard.writeText('{{ request.build_absolute_uri }}').then(() => {
      alert('Link copied to clipboard!');
    }, (err) => {
      console.error('Error copying link:', err);
      alert('Failed to copy link.');
    });
  });