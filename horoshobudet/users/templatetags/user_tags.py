from django import template
from django.db.models import Count

from users.models import TagMaster

register = template.Library()


@register.inclusion_tag('users/list_tags.html')
def show_all_tags():
    return {"tags": TagMaster.objects.annotate(total=Count("tags")).filter(total__gt=0)}