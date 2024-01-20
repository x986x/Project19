from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog import views

#from catalog.views import home, contacts

urlpatterns = [
    path('', views.index),
    path('contacts/', views.contacts),
    path ('products/', views.info_products),
    path ('catalogs/', views.catalogs)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)