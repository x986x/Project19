from django.shortcuts import render
from .models import  Product
# Create your views here.
def index(request):
    context={
        'products': Product.objects.all()
    }
    return render(request, 'catalog/index.html', context=context  )
def contacts(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
    print(request.method)
    return render(request, 'catalog/contacts.html')
def info_products(request):
    return render(request, 'catalog/info_products.html')