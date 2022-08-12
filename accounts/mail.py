from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

def email_confirmation(email, conf_number, url, first_name, last_name):
    subject=f'STAUD Agent Confirmation'
    body=f""
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=recipient_list)
    html_template = get_template('accounts/agent_confirmation.html').render(context={'email': email, "conf_number": conf_number, "url": url,
                                                                                    'first_name':first_name, 'last_name': last_name})
    message.attach_alternative(html_template, 'text/html')
    message.send()