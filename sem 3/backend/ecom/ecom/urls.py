"""
URL configuration for ecom project.
Routes admin and shop app URLs.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # Shop app at root
]
