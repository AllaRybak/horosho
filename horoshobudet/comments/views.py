from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import CommentForm, ContactUsCreateForm
from .models import Comment, ContactUs
from .utils import DataMixin, send_email_message


# Create your views here.
class AddComment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Функция отображения добавления комментария
    """
    form_class = CommentForm
    template_name = 'comments/add_comment.html'
    success_url = reverse_lazy('comments:all_comments')
    success_message = 'Спасибо за Ваш отзыв, он направлен модератору на проверку.'
    extra_context = {'title': 'Оставить отзыв - Всё будет хорошо'}

    def form_valid(self, form):
        comm = form.save(commit=False)
        comm.author = self.request.user
        return super().form_valid(form)


class CommentsList(ListView):
    """
    Представление отображения отзывов
    """
    model = Comment
    template_name = 'comments/comments.html'
    context_object_name = 'comments'
    extra_context = {'title': 'Отзывы - Всё будет хорошо'}
    paginate_by = 3

    def get_queryset(self):
        return Comment.is_published.all().select_related('author')


class ContactUsCreateView(DataMixin, SuccessMessageMixin, CreateView):
    """
    Представление для создания письма обратной связи
    """
    model = ContactUs
    form_class = ContactUsCreateForm
    template_name = 'comments/contact_us.html'
    success_url = reverse_lazy('home')
    success_message = 'Ваше письмо успешно отправлено. Благодарим за обращение.'

    def form_valid(self, form):
        if form.is_valid():
            contactus = form.save(commit=False)
            if self.request.user.is_authenticated:
                contactus.user = self.request.user
            send_email_message(contactus.subject, contactus.email, contactus.text_mes, contactus.user_id)
            # send_mail(contactus.subject, contactus.text_mes, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        context = dict(list(context.items()) + list(c_def.items()))
        return context
