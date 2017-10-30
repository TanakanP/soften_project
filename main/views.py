# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import EditForm, ImageUploadForm
from .models import Product, OrderBy, OrderList
from django.contrib.auth.models import User
from register.models import Profile
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from cart.forms import CartAddProductForm


import random
# Create your views here.

app_name = 'main'


def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {"product": product})


def product(request, product_id):
    product = Product.objects.all()
    number = Product.objects.get(pk=product_id)
    cart_product_form = CartAddProductForm()
    context = {"product": product,
               "number": number,
               "cart_product_form":cart_product_form,}
    return render(request, 'product.html', context)


def productnull(request):
    next = request.POST.get('next', '/catalog')
    return HttpResponseRedirect(next)


def catalog(request, gender="", product_brand=""):
    catalog = Product.objects.all()
    product = Product.objects.all()

    brandlist = []
    brandlist_Object = []
    for i in catalog:
        if not(i.brand in brandlist):
            brandlist.append(i.brand)
            brandlist_Object.append(i)

    if product_brand != "":
        catalog = catalog.filter(brand=product_brand)

    context = {"catalog": catalog,
               "product": product,
               "brandlist": brandlist_Object}

    return render(request, 'catalog.html', context)


def underconstruction(request):
    return render(request, 'underConstruction.html')


def contact(request):
    return render(request, 'contact.html')


def account(request, username):
    legit = False
    order = OrderBy.objects.filter(user_ID = request.user.profile)
    print(username)
    try:
        u = User.objects.get(username=username)
        p = Profile.objects.get(pk=u.pk)
        if(u.username == request.user.username):
            legit = True
        if request.method == 'POST':
            form = EditForm(data=request.POST, instance=u)
            print('yes')
            print(form.data['first_name'])

            if form.is_valid():
                u.first_name = form.cleaned_data.get('first_name')
                u.last_name = form.cleaned_data.get('last_name')
                u.email = form.cleaned_data.get('email')
                u.profile.address = form.cleaned_data.get('address')
                u.profile.phone = form.cleaned_data.get('phone')
                u.save()
                next = request.POST.get('next', '/home')
                return HttpResponseRedirect(next)
            else:
                print("KUY")
        else:
            form = EditForm(instance=u)
        context = {'form': form,
                   "legit": legit, "users": p, 'order': order, }
        return render(request, 'account.html', context)
    except:
        next = request.POST.get('next', '/home')
        return HttpResponseRedirect(next)


def accountnull(request):
    #        next = request.POST.get('next', '/home')
    return HttpResponseRedirect('/home')


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            u = request.user
            u.profile.pic = form.cleaned_data['image']
            u.save()
            return HttpResponse('image upload success')
    return render(request, 'uploadpic.html', {})

def history(request):
    order = OrderBy.objects.filter(user_ID = request.user.profile)

    context = { 'order': order}
    return render(request, 'history.html', context)

def orderdetail(request, order_id):
    order = OrderList.objects.filter(order_ID = order_id)
    orderd = OrderBy.objects.get(order_ID = order_id)
    context = { 'order': order,
    'orderd': orderd, }
    return render(request, 'orderdetail.html', context)
