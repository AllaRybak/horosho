from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Photos, Contract


# Register your models here.
class PhotosInline(admin.TabularInline):
    model = Photos
    extra = 5


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'is_onsite', 'content']
    list_display = ('id', 'name', 'is_onsite')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['-date_create']
    list_editable = ('is_onsite',)
    list_filter = ['is_onsite']
    search_fields = ['name']
    inlines = [PhotosInline,]
    list_per_page = 12
    save_on_top = True


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    fields = ['contract', 'photo', 'is_published', 'text']
    list_display = ('id', 'contract', 'get_html_photo', 'is_published')
    list_display_links = ('id',)
    list_editable = ('is_published',)
    list_filter = ['is_published']
    list_per_page = 12
    save_on_top = True

    def get_html_photo(self, examp):
        if examp.photo:
            return mark_safe(f"<img src='{examp.photo.url}' width=100>")
        else:
            return "Нет фото"

    get_html_photo.short_description = "Фото"
