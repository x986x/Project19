from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def my_custom_tag(photo):
    if 'http' in photo:
        return photo
    return photo
