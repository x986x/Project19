from django.contrib import admin
from .models import  Category, Product
#admin.site.register(Category )

@admin.register(Category )
class CategoryModelAdmin(admin.ModelAdmin):
    list_display =('id','name_category')


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'name_category','unit_price',)
    list_filter =('name_category',)
    search_fields =('message','name',)