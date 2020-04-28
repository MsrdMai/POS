
from . import views
from django.contrib import auth
from django.urls import path

urlpatterns = [
    
    path('product_add/', views.product_add, name='product_add'),
    path('type_add/', views.type_add, name='type_add'),
    path('type_delete/delete/<int:id>/', views.type_delete, name='type_delete'),
    path('type_edit/edit/<int:id>/', views.type_edit, name='type_edit'),
]
