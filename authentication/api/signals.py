from django.conf import settings
from django.db.models.signals import post_save
from user.models import User
from django.dispatch import receiver
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from config.config_settings import *

DOMAIN_FRONTEND = getattr(settings, 'DOMAIN_FRONTEND')

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created,**kwargs):
    if created:  
        subject = "Confirm your email"
        user = User.objects.get(email=instance.email)
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        context = {
            "username": "@" + instance.email.split('@')[0],
            "activate_link":f"{DOMAIN_FRONTEND}activate-account/{uid}/{token}/",
        }
        message = render_to_string("welcome.html", context)
        from_email = MAIL_USERNAME
        recipient_list = [instance.email, MAIL_USERNAME]
        email_to_send = EmailMessage( subject=subject,body=message,from_email=from_email,to=recipient_list) 
        email_to_send.content_subtype = "html"
        email_to_send.send()
    

