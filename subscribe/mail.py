from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

def unsubscribe_email(email):
    subject=f'You have successfully Unsubscribed'
    body=f"Please be sure to notify us if you had any problems. Thanks Management."
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=recipient_list)
    html_template = get_template('subscribe/email_unsubscribe.html').render()
    message.attach_alternative(html_template, 'text/html')
    message.send()

def subscribe_email(email, conf_number, url):
    subject=f'Thank You For Staudscribing!'
    body=f""
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=recipient_list)
    html_template = get_template('subscribe/subscribe_email.html').render(context={'email': email, "conf_number": conf_number, "url": url})
    message.attach_alternative(html_template, 'text/html')
    message.send()

def newsletter(subject, body, email):
    subject=subject
    body=body
    from_email=settings.EMAIL_HOST_USER
    recipient_list=email
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=recipient_list)
    html_template = get_template('subscribe/newsletter.html').render(context={'body': body})
    message.attach_alternative(html_template, 'text/html')
    message.send()