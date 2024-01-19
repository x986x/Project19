from django.apps import AppConfig
from django.template import Library
from catalog.templatetags import my_tags

class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    def ready(self):
        # Используйте simple_tag для регистрации вашего тега
        register = Library()
        register.simple_tag(my_tags.my_custom_tag)
