
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from management.models import Product, Type
from django.shortcuts import get_object_or_404
from django.db import models
from django.template.context_processors import request
# Create your views here.
# from django import forms
# from management.forms import ProductForm
from django.db import IntegrityError


def type_add(request):

    context = {}

    typess = Type.objects.all()
    if request.method == 'GET':
        name = request.GET.get('name')
        description = request.GET.get('description')
        try:
            type_obj= Type(name=name, description=description)
            type_obj.save() 
            msg = 'Successfully'
        except:
            msg = 'wait'
            
       
    context = {
        'msg': msg,
        'typess' : typess
    }


    return render(request, template_name='product/type_add.html' , context=context) 


def type_delete(request, id):
    types = Type.objects.get(id=id)
    types.delete()
    txt = 'Remove Successfully'
    typess = Type.objects.all()
    context = {'typess' : typess,
            'txt' : txt
    }
    return render(request, template_name='product/type_add.html', context=context)


def type_edit(request, id):
    context = {}
    msg = ''
    try:
        type2 = Type.objects.get(pk=id)
    except Type.DoesNotExist:
        return redirect(to='ad่justlist')

    
    if request.method == 'GET':
        try:
            type2.name=request.GET.get('name')
            type2.description=request.GET.get('description')
            type2.save()
            msg = 'Successfully update Type - Name: %s' % (type2.name)
        except IntegrityError as e:
            msg = '...'
            type2 = Type.objects.get(pk=id)

    context = {

        'type2': type2,
        'msg': msg,
    }

    return render(request, template_name='product/type_edit.html', context=context)


def product_add(request):
    """
        เพิ่ม product

    """
    context = {}
    msg = 'wait'
    typess = Type.objects.all() 

    if request.method == 'GET':
        try:
            product_info = Product.objects.create(types_id=request.GET.get('types_id'), name=request.GET.get('proname'),
                        price=request.GET.get('proprice'), description= request.GET.get('prodescription'))
       
       
            product_info.save()
            msg = 'Successfully'
        
        except IntegrityError as e:
            msg = '...'
            
    else:
        product_info =  Product.objects.none()

    
    context = {
        'typess' : typess,
        'msg' : msg,
    }
    return render(request, template_name='product/product_add.html', context=context)

