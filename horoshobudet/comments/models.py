from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.deconstruct import deconstructible


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя"
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Отзывы просим написать на русском языке."

    def __call__(self, value):
        if len(set(value) & set(self.ALLOWED_CHARS)) <= 1:
            raise ValidationError(self.message, code=self.code, params={"value": value})


CustomUser = get_user_model()


class PublishedManager(models.Manager):
    """Мэнеджер записей Опубликован комментарий """
    def get_queryset(self):
        return super().get_queryset().filter(published=True)


# Create your models here.
class Comment(models.Model):
    """
    Модель отзывов
    """
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user', verbose_name="Автор")
    comment = models.CharField(max_length=500, verbose_name="Комментарий",
                               validators=[RussianValidator()])
    published = models.BooleanField(default=False, verbose_name="Статус")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    objects = models.Manager()
    is_published = PublishedManager()

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-date_create', 'author']

    def __str__(self):
        return self.comment


class ContactUs(models.Model):
    """
    Модель обратной связи
    """
    subject = models.CharField(max_length=100, verbose_name='Тема обращения')
    email = models.EmailField(max_length=255, verbose_name='email')
    text_mes = models.TextField(verbose_name='Текст', max_length=500)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    user = models.ForeignKey(CustomUser, verbose_name='От', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
        ordering = ['-time_create']

    def __str__(self):
        return f'Новое сообщение от {self.email}'
