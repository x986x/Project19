from django.shortcuts import render

def index(request):
    # Ваш код для представления index
    return render(request, 'catalog/index.html')

def contacts(request):
    # Ваш код для представления contacts
    return render(request, 'catalog/contacts.html')

def info_products(request):
    # Ваш код для представления info_products
    return render(request, 'catalog/info_products.html')