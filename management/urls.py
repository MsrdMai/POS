from django.contrib import auth
from django.urls import path

from . import views


urlpatterns = [
    path('', views.my_login, name='login'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('index/', views.index, name='index'),
    path('ad่justlist/', views.ad่justlist, name='ad่justlist'),
    path('ad่justlist/delete/<int:id>', views.product_delete, name='product_delete'),
    path('ad่justlist/edit/<int:id>/', views.edit, name='edit'),
    path('index/add_cart/<int:id>/', views.add_cart, name='add_cart'),
    path('index/cart_delete/<int:id>/', views.cart_delete, name='cart_delete'),
]
