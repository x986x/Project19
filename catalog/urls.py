from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

from catalog.views import IndexListView, ProductsDetailView, CatalogsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('base/', IndexListView.as_view(), name='index'),
    path('contacts/', views.contacts),
    path('products/<int:pk>/', ProductsDetailView.as_view(), name='product-detail'),
    path('catalogs/', CatalogsListView.as_view(), name='catalogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
