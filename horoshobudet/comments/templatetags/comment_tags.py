from django import template

from ..models import Comment

register = template.Library()


@register.simple_tag
def total_comments():
    return Comment.is_published.select_related('published').count()
