import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseNotFound
import json


def index(request):
    products_file_path = os.path.join(settings.BASE_DIR, 'media', 'products.json')
    with open(products_file_path, 'r', encoding='utf-8') as file:
        products = json.load(file)
    return render(request, 'catalog/catalogs.html', {'products': products})


def contacts(request):
    # Ваш код для представления contacts
    return render(request, 'catalog/contacts.html')


def info_products(request, product_id):
    products_file_path = os.path.join(settings.BASE_DIR, 'media', 'products.json')
    with open(products_file_path, 'r', encoding='utf-8') as file:
        products = json.load(file)

    product = None
    for p in products:
        if p.get('pk') == product_id:
            product = p
            break

    if product:
        return render(request, 'catalog/info_products.html', {'product': product})
    else:
        # Обработка случая, когда товар с указанным ID не найден
        return HttpResponseNotFound('Product not found')


def catalogs(request):
    products_file_path = os.path.join(settings.MEDIA_ROOT, 'products.json')
    with open(products_file_path, 'r', encoding='utf-8') as file:
        products = json.load(file)
    return render(request, 'catalog/catalogs.html', {'products': products})


