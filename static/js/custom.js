document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");

  // Initialize Section Titles for dynamic navbar subtitle
  initSectionTitles();
  initActiveNavLinks();
  initShareAndCopyButtons();
  initVoteButtons();
});

function initSectionTitles() {
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
}

function initActiveNavLinks() {
  const pathname = window.location.pathname;
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
  const navbarTitle = document.getElementById("navbar-title");

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

function initShareAndCopyButtons() {
  const shareBtn = document.getElementById("shareBtn");
  const fallbackShare = document.getElementById("fallbackShare");
  const copyBtn = document.getElementById("copyBtn");

  shareBtn.addEventListener("click", function () {
    if (navigator.share) {
      navigator
        .share({
          title: "{{ blogpost.title }}",
          url: window.location.href,
        })
        .catch(console.error);
    } else {
      if (
        fallbackShare.style.display === "none" ||
        fallbackShare.style.display === ""
      ) {
        fallbackShare.style.display = "block";
        setTimeout(() => (fallbackShare.style.opacity = "1"), 10);
      } else {
        fallbackShare.style.opacity = "0";
        setTimeout(() => (fallbackShare.style.display = "none"), 250);
      }
    }
  });

  copyBtn.addEventListener("click", function () {
    navigator.clipboard
      .writeText(window.location.href)
      .then(() => alert("Link copied to clipboard!"))
      .catch(() => alert("Failed to copy link."));
  });
}

function initVoteButtons() {
  const voteButtons = document.querySelectorAll(".vote-button");
  console.log("Vote buttons found:", voteButtons.length);

  voteButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const voteType = this.dataset.voteType;
      const postId = this.dataset.postId;
      console.log(
        "Button clicked for vote type:",
        voteType,
        "on post:",
        postId
      );
      submitVote(voteType, postId);
    });
  });

  function submitVote(voteType, postId) {
    const csrfToken = getCsrfToken();
    console.log("Submitting vote with CSRF Token:", csrfToken);

    fetch(`/blog/post/${postId}/vote/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify({ vote: voteType }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Received response:", data);
        if (data.success) {
          updateVoteResults(data.percentages);
        } else {
          console.error("Error submitting vote:", data.error);
        }
      })
      .catch((error) => {
        console.error("Error submitting vote:", error);
      });
  }

  function getCsrfToken() {
    let csrfToken = "";
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      let [name, value] = cookie.trim().split("=");
      if (name === "csrftoken") {
        csrfToken = value;
        break;
      }
    }
    return csrfToken;
  }

  function updateVoteResults(percentages) {
    Object.entries(percentages).forEach(([key, value]) => {
      const percentSpan = document.getElementById(`vote_${key}_percent`);
      if (percentSpan) {
        percentSpan.textContent = `${parseFloat(value).toFixed(1)}%`;
      }
    });
    showFeedback("Thanks for your feedback!");
  }

  function showFeedback(message) {
    const feedbackElement = document.getElementById("vote-feedback");
    if (feedbackElement) {
      feedbackElement.textContent = message;
      feedbackElement.classList.add("show");

      setTimeout(() => {
        feedbackElement.classList.remove("show");
      }, 4000);
    }
  }
}
