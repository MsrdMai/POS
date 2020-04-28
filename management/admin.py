from django.contrib import admin
from django.contrib.auth.models import Permission
from webbrowser import register
from management.models import Order, Order_Product, Product, Type

# Register your models here.



# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 1



class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_per_page = 10

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'types', 'price']
    list_per_page = 10


class Order_ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id','product_id', 'amount']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time','total_price']

admin.site.register(Permission)
admin.site.register(Product, ProductAdmin) # ใส่models
admin.site.register(Type, TypeAdmin)
admin.site.register(Order_Product, Order_ProductAdmin)
admin.site.register(Order, OrderAdmin)
