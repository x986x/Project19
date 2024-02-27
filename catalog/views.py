from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'products': products})


def contacts(request):
    # Ваш код для представления contacts
    return render(request, 'catalog/contacts.html')


def info_products(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        return render(request, 'catalog/info_products.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponseNotFound('Product not found')


def catalogs(request):
    products = Product.objects.all()
    return render(request, 'catalog/catalogs.html', {'products': products})
