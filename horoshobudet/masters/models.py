from django.db import models
# from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe


# from django.utils.translation import gettext_lazy as _
# from taggit.managers import TaggableManager


# Create your models here.
class Photos(models.Model):
    """ Модель фотографий с объектов - примеры"""
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, blank=True, verbose_name='Адрес объекта',
                                 related_name='photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name="Фотоотчет")
    text = models.TextField(blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Фото объекта'
        verbose_name_plural = 'Фото объекта'


class Contract(models.Model):
    """ Модель с адресами объектов выполенных работ"""
    name = models.CharField(max_length=50, db_index=True, verbose_name='Адрес (название) объекта')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='slug')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    content = models.CharField(max_length=250, blank=True, verbose_name='Дополнительная информация')
    is_onsite = models.BooleanField(default=False, verbose_name='Опубликовано')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Объекты'
        verbose_name_plural = 'Объект'
        ordering = ['date_create']

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('contract_list', args=[str(self.pk)])
