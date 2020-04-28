
import datetime
from builtins import object
from venv import create

import pkg_resources
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import request

from management.models import Order, Order_Product, Product, Type

# from management.models import ClassRoom

# Create your views here.

def my_login(request):
    
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            # return redirect(to='index')
            if user:
                login(request, user)
                next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
    
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = "Wrong username or password!!!"

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

           

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect(to='login')



@login_required
@permission_required('management.adjustlist')
def ad่justlist(request):
    typess = Type.objects.all()
    search_txt = request.GET.get('inputSearch', '')
    print(search_txt)
    semester = request.GET.get('semester', '')

    object_list = Product.objects.filter(
        name__icontains=search_txt
    )
    if semester:
        object_list = object_list.filter(types=semester)
    
    return render(request, 'management/ad่justlist.html', context={
        'search_txt': search_txt,
        'semester': semester,
        'object_list': object_list,
        'typess' : typess
    })


def product_delete(request, id):
    """
        ลบข้อมูล product โดยลบข้อมูลที่มี id 
    """
    object_list = Product.objects.get(id=id)
    object_list.delete()
   
    return redirect(to='ad่justlist')



def edit(request, id):
    context = {}
    msg = ''
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return redirect(to='ad่justlist')

    typess = Type.objects.all()
    if request.method == 'GET':
        try:
            product.name=request.GET.get('name')
            product.types_id=request.GET.get('types')
            product.price=request.GET.get('price')
            product.description=request.GET.get('description')
            product.save()
            msg = 'Successfully update Product - Name: %s' % (product.name)
        except IntegrityError as e:
            msg = '...'
            product = Product.objects.get(pk=id)

    context = {

        'typess': typess,
        'product': product,
        'msg': msg,
    }

    return render(request, template_name='product/edit.html', context=context)

def cart_delete(request, id):
    """
        เกิด MultipleObjectsReturned error in django เลยให้เรียงด้วยไอดีแล้วเอาไอดีที่ซ้ำอันแรกออก กรณีไอดีสินค้าเดียวกัน

    """

    list_order = Order_Product.objects.filter(product_id_id=id).order_by('id').first()
    list_order.delete()

    return redirect(to='index')



def add_cart(request, id):

    msg = '...'
    check = True
    num_id = 1
    while check == True:
        
        # product = Product.objects.get(pk=id) #เอาไอดีสินค้าเพื่อเอาสินค้าใส่ในProduct_order
        # amount = 1
        # list_order = Order_Product.objects.create(product_id_id=product.id, amount=amount, order_id_id=num_id) # ใส่ไอดีorder
        # list_order.save()
        # msg = 'Successfully'
        # num_id += 1
        # check = False
        product = Product.objects.get(pk=id)
        amount = 1
        try:
            order = Order.objects.get(total_price=0)
            if order:
                list_order = Order_Product.objects.create(product_id_id=product.id, amount=amount, order_id_id=order.id)
                list_order.save()
                msg = 'Successfully'
                check = False
        except:
            order = Order(total_price=0)
            order.save()


    context = {
        'product' : product,
        'msg' : msg,
        'list_order' : list_order

    }

    return render(request, 'management/add_cart.html', context=context)



def index(request):
    """
        แสดงข้อมูล product ทั้งหมดในระบบ
    """
    # return render(request, 'management/index.html')
    typess = Type.objects.all()
    search_txt = request.GET.get('inputSearch', '')
    print(search_txt)
    semester = request.GET.get('semester', '')

    object_list = Product.objects.filter(
        name__icontains=search_txt
    )
    if semester:
        object_list = object_list.filter(types=semester)


    total = 0
    count = 0
    
    try:
        cart = Order.objects.get(total_price=0) #สร้าง0มาก่อนถึงเวลาเรียกใช้ก็จะเซฟเวลาทับให้เลย
    except:
        cart = Order(total_price=0)
        cart.save()
    
    if cart:
        list_order = Order_Product.objects.filter(order_id_id=cart.id)
        for i in list_order:
            total += i.product_id.price
            count += i.amount
        if request.method == 'POST':
            cart.total_price= total
            cart.save()
    else:
        list_order = Order_Product.objects.latest('id')

    return render(request, 'management/index.html', context={
        'search_txt': search_txt,
        'semester': semester,
        'object_list': object_list,
        'typess' : typess,
        'list_order' : list_order,
        'total' : total,
        'count' : count
 
    })

    # list_order = Order_Product.objects.filter(order_id_id=id)

    # total = 0
    # count = 0
    # for i in list_order:
    #     total += i.product_id.price
    #     count += i.amount
        
    # if request.method == 'POST':
    #     cart = Order.objects.get(pk=id)
    #     cart.total_price= total
    #     cart.save()
    #     id += 1
    #     list_order = Order_Product.objects.filter(order_id_id=id)
    #     total = 0
    #     count = 0


