document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");

  // Cycle through section titles for dynamic navbar subtitle
  const sectionTitles = document.querySelectorAll("h1, h2, h3, h4");
  const navbarTitle = document.getElementById("navbar-title");
  const navbarSubtitle = document.getElementById("navbar-subtitle");
  let currentTitleIndex = 0;

  function cycleSectionTitles() {
    console.log("Cycling through section titles");
    if (sectionTitles.length > 0) {
      navbarSubtitle.style.opacity = 0;
      setTimeout(function () {
        navbarSubtitle.textContent =
          sectionTitles[currentTitleIndex].textContent;
        navbarSubtitle.style.opacity = 1;
        currentTitleIndex = (currentTitleIndex + 1) % sectionTitles.length;
      }, 1500);
    }
  }

  cycleSectionTitles();
  setInterval(cycleSectionTitles, 8000);

  const pathname = window.location.pathname;
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

  function setActiveNavLink() {
    console.log("Setting active nav link");
    let section = "home";
    navbarTitle.style.opacity = "0";

    setTimeout(() => {
      let iconHtml = "";
      let sectionText = "";
      if (pathname.includes("services")) {
        section = "services";
        iconHtml = '<i class="fas fa-briefcase"></i>';
        sectionText = "Services";
      } else if (pathname.includes("blog")) {
        section = "blog";
        iconHtml = '<i class="fas fa-blog"></i>';
        sectionText = "Blog";
      } else if (pathname.includes("appointments")) {
        section = "appointments";
        iconHtml = '<i class="fas fa-calendar-check"></i>';
        sectionText = "Appointments";
      } else {
        iconHtml = '<i class="fas fa-home"></i>';
        sectionText = "Home";
      }

      navbarTitle.innerHTML = `${sectionText} ${iconHtml}`;
      navbarTitle.style.opacity = "1";

      navLinks.forEach((link) => {
        link.classList.remove("nav-active");
        if (link.getAttribute("href").includes(section)) {
          link.classList.add("nav-active");
        }
      });
    }, 500);
  }

  setActiveNavLink();

  // Toggle Share Links
  const shareBtn = document.getElementById("shareBtn");
  if (shareBtn) {
    shareBtn.addEventListener("click", function () {
      const shareLinks = document.getElementById("fallbackShare");
      if (navigator.share) {
        navigator
          .share({
            title: document.title,
            url: window.location.href,
          })
          .then(() => console.log("Content shared successfully"))
          .catch((err) => console.error("Error sharing:", err));
      } else {
        console.log("Navigator share not available. Showing fallback.");
        shareLinks.style.display =
          shareLinks.style.display === "none" ? "block" : "none";
      }
    });
  }

  // Copy button functionality
  const copyBtn = document.getElementById("copyBtn");
  if (copyBtn) {
    copyBtn.addEventListener("click", function () {
      navigator.clipboard
        .writeText(window.location.href)
        .then(() => {
          alert("Link copied to clipboard!");
          console.log("Link copied successfully");
        })
        .catch((err) => {
          console.error("Error copying link:", err);
          alert("Failed to copy link.");
        });
    });
  }
});

document.addEventListener('DOMContentLoaded', function () {
  console.log("DOM fully loaded and parsed");

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie('csrftoken');

  const voteForm = document.querySelector('form.poll-voting-section');
  if (voteForm) {
    voteForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const formData = new FormData(voteForm);

      fetch(voteForm.action, {
        method: 'POST',
        body: formData,
        headers: {
          'X-CSRFToken': csrftoken
        },
        credentials: 'same-origin'
      })
      .then(response => response.json())
      .then(data => {
        data.pollOptions.forEach(option => {
          const bar = document.querySelector(`.progress-bar[data-option-id="${option.id}"]`);
          if (bar) {
            bar.style.width = `${option.percentage}%`;
            bar.setAttribute('aria-valuenow', option.percentage);

            const percentageDisplay = bar.parentNode.querySelector('.percentage-display');
            if (percentageDisplay) {
              percentageDisplay.textContent = `${option.percentage}%`;
            }
          }
        });
      })
      .catch(error => console.error('Error submitting vote:', error));
    });
  }

  document.querySelectorAll('.progress-bar').forEach(function (bar) {
    const percentage = bar.getAttribute('data-percentage');
    bar.style.width = `${percentage}%`;
  });
});
