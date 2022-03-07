
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from project import settings

@shared_task(bind=True)
def send_emails(self):
    users=get_user_model().objects.all()
    for user in users :
        subject='Celery Testing'
        message='Good Morning, have a good day '
        from_email=settings.EMAIL_HOST_USER 
        to_email=user.email
        send_mail( 
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[to_email],
            fail_silently=True
        )
    return 'Done'