from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/',views.product, name="product"),
    path('checkout/',views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name = 'update_item'),
    path('cart/',views.cart, name="cart"),
    path('detail/',views.detail, name="detail"),
    path('search_page/', views.searchpage, name='search_page')
]