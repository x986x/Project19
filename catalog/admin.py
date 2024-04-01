from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('title', 'description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk','product', 'version_number', 'version_title','is_active',)
    list_filter = ('product',)