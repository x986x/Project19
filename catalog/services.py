from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_categories():

    if settings.CACHE_ENABLED:
        key = 'category_list.html'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()

    return category_list