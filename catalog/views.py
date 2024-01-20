from django.shortcuts import render
import json

def index(request):
    # Ваш код для представления index
    return render(request, 'catalog/index.html')

def contacts(request):
    # Ваш код для представления contacts
    return render(request, 'catalog/contacts.html')

def info_products(request):
    # Ваш код для представления info_products
    return render(request, 'catalog/info_products.html')


def catalogs(request):
    with open('catalog/fixtures/products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)
    print(products)
    # Передача объекта в контекст шаблона
    return render(request, 'catalog/catalogs.html', {'products': products})
