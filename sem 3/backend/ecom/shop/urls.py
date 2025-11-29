"""
URL patterns for the shop app.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'shop'

urlpatterns = [
    # Product views
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='category_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Cart views
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),

    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/complete/<int:order_id>/', views.checkout_complete, name='checkout_complete'),

    # Auth views
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
