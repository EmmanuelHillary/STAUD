from django.core.mail import send_mail
from django.conf import settings


def contact_us(name, email, message):
    subject=f'Contact Us {email}: Enquiries'
    body=f"{message}"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[settings.ADMIN_HOST_USER]
    send_mail(subject, body, email, recipient_list)