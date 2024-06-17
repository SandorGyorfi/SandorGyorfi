from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import logging

# Setting up logging
logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Prepare the email content
            html_content = render_to_string('emails/contact_confirmation.html', {'contact': contact})
            text_content = strip_tags(html_content)

            try:
                send_mail(
                    subject='Thank you for contacting me!',
                    message=text_content,
                    from_email='request@sandorgyorfi.com',
                    recipient_list=[contact.email],
                    html_message=html_content,
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully! Check your email for confirmation.')
            except Exception as e:
                logger.error("Error sending email: %s", e)
                messages.error(request, 'We encountered a problem sending your email. Please try again later.')

            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})
