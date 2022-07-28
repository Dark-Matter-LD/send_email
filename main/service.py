from django.core.mail import send_mail

def send(user_email):
    send_mail(
        subject ='Вы подписались на рассылку',
        message = 'Не надо от нее отписываться' ,
        from_email = 'jangonepobezhdenniy@yandex.ru',
        recipient_list = [user_email],
        fail_silently=False
    )