from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from comments.models import CustomUser

menu = [{'title': 'Обратная связь', 'url_name': 'about'},
        {'title': 'Отзывы', 'url_name': 'comments'},
        ]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context


def send_email_message(subject, email, text_mes, user_id):
    """
    Функция отправки сообщений от пользователя
    """
    if user_id:
        user = CustomUser.objects.get(id=user_id)
    else:
        user = None
    message = render_to_string('comments/contactus_email_send.html', {
        'email': email,
        'text_mes': text_mes,
        'user': user,
    })
    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
    email.send(fail_silently=False)
