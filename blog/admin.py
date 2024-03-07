from django.contrib import admin

from blog.models import Blog


# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'body', 'preview', 'date_of_creation',)