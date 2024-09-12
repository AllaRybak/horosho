from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView
# таги по Меле
# from taggit.models import Tag

from users.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from users.models import TagMaster
from users.utils import DataMixin


# Create your views here.
class RegisterUser(CreateView):
    """
    Представление регистрации
    """
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')


class LoginUser(LoginView):
    """
    Представление авторизации
    """
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}


def logout_user(request):
    """
    Представление выхода из авторизации
    """
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class ProfileUser(LoginRequiredMixin, DataMixin, SuccessMessageMixin, UpdateView):
    """
    Представление изменения аккаунта
    """
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    page_title = 'Профиль пользователя - Всё будет хорошо'
    default_image = '/media/users/user-gear-solid.svg'
    success_message = 'Профиль сохранён.'

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        if not form.instance.is_master:
            form.instance.content = None
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context)

    def get_success_url(self):
        if not self.request.user.is_master:
            self.request.user.tags.clear()
        return reverse_lazy('users:profile')


class UserPasswordChange(PasswordChangeView):
    """
    Представление смены пароля
    """
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}


class UserList(DataMixin, ListView):
    """
    Список всех мастеров
    """
    template_name = "users/masters.html"
    context_object_name = 'masters'
    page_title = 'Найти мастера - Всё будет хорошо'
    default_image = '/media/users/user-solid.svg'

    def get_queryset(self):
        return get_user_model().ismaster.all()


class MasterDetail(DataMixin, DetailView):
    """Отображение клиента"""
    template_name = 'users/master.html'
    slug_url_kwarg = 'master_slug' # стандартный атрибут = ...
    context_object_name = 'master'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['master'].username)

    def get_object(self, queryset=None):
        return get_object_or_404(get_user_model().ismaster, slug=self.kwargs[self.slug_url_kwarg])


class TagMastersList(DataMixin, ListView):
    template_name = 'users/masters.html'
    context_object_name = 'masters'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagMaster.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title='Наши мастеры с навыком: ' + tag.tag)

    def get_queryset(self):
        return get_user_model().ismaster.filter(tags__slug=self.kwargs['tag_slug'])


# List Tag Mele
# class MastersByTagListView(ListView):
#     model = get_user_model()
#     template_name = 'users/masters-mele.html'
#     context_object_name = 'masters'
#     tags = Tag.objects.all()
#     tag = None
#
#     def get_queryset(self):
#         self.tag = Tag.objects.get(slug=self.kwargs['tag_slug'])
#         return get_user_model().ismaster.all().filter(tags_mele__slug=self.tag.slug)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = f'Статьи по тегу: {self.tag.name}'
#         context['tags'] = self.tags
#         return context
#
#     def get_absolute_url(self):
#         return reverse('users:masters_list_by_tag', kwargs={'tag_slug': self.tag.slug})

