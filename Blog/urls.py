from django.urls import path

from Blog.apps import BlogConfig
from Blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toogle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toogle_activity, name='toogle_activity'),

]