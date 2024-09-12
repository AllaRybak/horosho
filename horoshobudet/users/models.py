from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


# Create your models here.
class IsMasterManager(models.Manager):
    """Мэнеджер записей пользователей с фильтром "Мастер" """
    def get_queryset(self):
        return super().get_queryset().filter(is_master=True)


class User(AbstractUser):
    """
    Модель пользователя расширенная
    """
    class Status(models.IntegerChoices):
        KLIENT = 0, 'Обычный пользователь'
        PROFI = 1, 'Мастер'
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True, verbose_name='Фотография')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='slug')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = PhoneNumberField(max_length=12, blank=True, null=True, unique=True, verbose_name='Телефон')
    is_master = models.BooleanField(default=Status.KLIENT, verbose_name="Статус мастера")
    content = models.TextField(max_length=800, null=True, blank=True, verbose_name='О мастере')

    tags = models.ManyToManyField('TagMaster', blank=True, related_name='tags', verbose_name='Навыки')

    objects = UserManager()
    ismaster = IsMasterManager()

    def get_absolute_url(self):
        return reverse('users:master', kwargs={'master_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.username))
        super().save(*args, **kwargs)


class TagMaster(models.Model):
    """Модель тэгов (many-to-many)"""
    tag = models.CharField(max_length=100, db_index=True, verbose_name='навык')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Навыки (тэги)'
        ordering = ['tag']

    def get_absolute_url(self):
        return reverse('users:tag', kwargs={'tag_slug': self.slug})

    def __str__(self):
        return self.tag
