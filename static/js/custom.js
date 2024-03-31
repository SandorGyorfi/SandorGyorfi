document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");

  // Cycle through section titles for dynamic navbar subtitle
  const sectionTitles = document.querySelectorAll("h2, h3");
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
      }, 500);
    }
  }

  cycleSectionTitles();
  setInterval(cycleSectionTitles, 4000);

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


