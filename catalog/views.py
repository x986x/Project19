from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'


def contacts(request):
    # Ваш код для представления contacts
    return render(request, 'catalog/contacts.html')


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/info_products.html'


class CatalogsListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'