from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def my_custom_tag(photo):
    # Используйте функцию static для формирования правильного URL статического файла
    photo_url = static(photo)
    return photo_url
