from django.contrib import admin

# Register your models here.
from django.contrib import admin


from users.models import User, TagMaster


class PhoneNumberFilter(admin.SimpleListFilter):
    title = "Указан номер телефона"
    parameter_name = 'phone'

    def lookups(self, request, model_admin):
        return [
            ('with', 'С телефоном'),
            ('without', 'Без телефона'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'with':
            return queryset.filter(phone_number__isnull=False)
        elif self.value() == 'without':
            return queryset.filter(phone_number__isnull=True)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'slug', 'email', 'phone_number', 'tags', 'is_master', 'content']
    list_display = ('id', 'username', 'photo', 'first_name', 'last_name', 'phone_number', 'is_master', 'get_tags')
    list_display_links = ('id', 'username')
    filter_vertical = ['tags']
    prepopulated_fields = {'slug': ('username',)}
    ordering = ['-is_master', 'first_name']
    search_fields = ['first_name', 'phone_number']
    list_filter = ['tags__tag', 'is_master', PhoneNumberFilter]
    list_per_page = 12

    @admin.display(description='навыки')
    def get_tags(self, obj):
        return [tag.tag for tag in obj.tags.all()]


@admin.register(TagMaster)
class TagMasterAdmin(admin.ModelAdmin):
    list_display = ('tag', 'slug')
    prepopulated_fields = {'slug': ('tag',)}