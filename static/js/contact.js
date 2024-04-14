document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".contact-form");
    const actionUrl = form.getAttribute('data-action-url');
    const messageContainer = document.querySelector('.alert-messages');  

    if (messageContainer) {
        form.addEventListener("submit", function(event) {
            event.preventDefault();
            const formData = new FormData(form);

            fetch(actionUrl, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            }).then(_ => {
                messageContainer.innerHTML = '<div class="alert alert-success" role="alert">Message sent successfully!</div>';
                form.reset(); 
            }).catch(_ => {
                messageContainer.innerHTML = '<div class="alert alert-danger" role="alert">Failed to send the message.</div>';
            });
        });
    } else {
        console.error("Message container not found, cannot display messages.");
    }
});

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

document.addEventListener('DOMContentLoaded', function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.display = 'none';
        }, 5000);
    });
});