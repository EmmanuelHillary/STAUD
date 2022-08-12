from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

def order_email_to_staud(name, budget, phone, occupation, email, accommodation_type, campus, location, agency, room_size, furnished, comment):
    subject=f'Your Order Was Successful'
    body=f"We would give you an update when your order is ready."
    from_email=settings.EMAIL_HOST_USER
    recipient_list=[email]
    message = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=recipient_list)
    context = {
        'name': name, 'budget': budget, 'phone': phone, 'occupation': occupation, 'email': email, 'accommodation_type': accommodation_type, 'campus': campus, 'location': location,
        'agency': agency, 'room_size': room_size, 'furnished': furnished, 'comment': comment
    }
    html_template = get_template('order/email_order.html').render(context=context)
    message.attach_alternative(html_template, 'text/html')
    message.send()