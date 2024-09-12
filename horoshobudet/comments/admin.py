from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Админ-панель модели Обратная связь
    """
    list_display = ('email', 'user', 'time_create', 'time_create')
    list_display_links = ('email',)
    readonly_fields = ['email', 'user', 'subject', 'text_mes']
    list_per_page = 12


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Админ-панель модели Отзызы
    """
    list_display = ('author', 'comment', 'published', 'date_create')
    list_display_links = ('comment',)
    readonly_fields = ['author', 'comment']
    list_editable = ('published',)
    list_filter = ('published', )
    list_per_page = 12
    save_on_top = True
