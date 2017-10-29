# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import EditForm, ImageUploadForm
from .models import Product, Prod4, Prod360
from django.contrib.auth.models import User
from register.models import Profile
from django.http import HttpResponseRedirect
from django.http import HttpResponse

import random
# Create your views here.

app_name = 'main'


def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {"product": product})


def product(request, product_id):
    product = Product.objects.all()
    number = Product.objects.get(pk=product_id)
    pic_format = Product.format(number)
    if pic_format == 4:
        path = Prod4.objects.all()
    else :
        path = Prod360.objects.all()
    context = {"product": product,
               "number": number,
               "path": path,
               "pic_format": pic_format,}
    return render(request, 'product.html', context)


def productnull(request):
    next = request.POST.get('next', '/catalog')
    return HttpResponseRedirect(next)


def catalog(request, gender="", product_brand=""):
    catalog = Product.objects.all()
    product = Product.objects.all()
    pic_type_4 = Prod4.objects.all()
    pic_type_360 = Prod360.objects.all()

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
               "brandlist": brandlist_Object,
               "path4": pic_type_4,
               "path360": pic_type_360}

    return render(request, 'catalog.html', context)


def underconstruction(request):
    return render(request, 'underConstruction.html')


def contact(request):
    return render(request, 'contact.html')


def account(request, username):
    legit = False
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
                   "legit": legit, "users": p}
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
