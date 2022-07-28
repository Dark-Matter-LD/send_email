from send_email.celery import app
from django.core.mail import send_mail

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)

   
@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
        subject ='Смотри, что нашёл',
        message = 'Вы подписались на спам рассылку, это сообщение будет отправляться каждую минуту' ,
        from_email = 'jangonepobezhdenniy@yandex.ru',
        recipient_list = [contact.email],
        fail_silently=False
    )