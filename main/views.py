# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import EditForm, ImageUploadForm
from .models import Product, Prod4, Prod360, OrderBy, OrderList, Supplier,NewS
from django.contrib.auth.models import User
from register.models import Profile
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from cart.cart import Cart

import random
# Create your views here.

app_name = 'main'


def edit_sale():
    product = Product.objects.all()
    for i in product:
        i.saved()
    return 0

def update(request):
    product = Product.objects.all()
    t = edit_sale()
    for i in product:
        print(i.product_ID,"  " ,i.unit_Price_Sale)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)

def home(request):
    product = Product.objects.all()
    # t = edit_sale()
    # for i in product:
    #     print(i.product_ID,"  " ,i.unit_Price_Sale)
    return render(request, 'home.html', {"product": product})



def product(request, product_id=""):
    cart = Cart(request)
    product = Product.objects.all()
    try:
        number = Product.objects.get(pk=product_id)
        cart_product_form = CartAddProductForm()
        pic_format = Product.format(number)
        logo = Product.get_brand(number)
        logo_path = Supplier.objects.all()

        if pic_format == 4:
            path = Prod4.objects.all()
        else :
            path = Prod360.objects.all()

        context = {"product": product,
                   "number": number,
                   "path": path,
                   "pic_format": pic_format,
                   "cart_product_form":cart_product_form,
                   "logo_path": logo_path,
                   "logo": logo,
                   "cart": cart,}
        return render(request, 'product.html', context)
    except Exception as e:
        next = request.POST.get('next', '/catalog')
        return HttpResponseRedirect(next)


def catalog(request, product_brand="",key_sort="name"):
    cart = Cart(request)
    brandcheck = []
    gendercheck = []
    brandcheck = request.POST.getlist("radio-set-2")
    gendercheck = request.POST.getlist("radio-set-1")
    allcheck = request.POST.getlist("radio-set-3")
    keycheck = request.POST.getlist("key")
    catalog = Product.objects.all()
    product = Product.objects.all()
    pic_type_4 = Prod4.objects.all()
    pic_type_360 = Prod360.objects.all()

    brandlist = []

    for i in catalog:
        if not(i.brand in brandlist):
            brandlist.append(i.brand)

    if "All" in brandcheck or allcheck == "All" or not brandcheck:
        brandcheck = brandlist

    if "All" in gendercheck or allcheck == "All" or not gendercheck:
        gendercheck = ["M","F"]

    if product_brand in brandlist:
        brandcheck = [product_brand]


    if key_sort == 'promotion':
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-promotion')
    elif key_sort == 'name':
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-product_Name')
    elif key_sort == 'price':
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-unit_Price_Sale')

    if brandcheck == brandlist:
        brandcheck = ["All"]

    if gendercheck == ["M","F"]:
        gendercheck = ["All"]

    if brandcheck == ["All"] and gendercheck == ["All"] :
        allcheck = 'All'

    context = {"catalog": trueCatalog,
               "product": product,
               "brandlist": brandlist,
               "path4": pic_type_4,
               "path360": pic_type_360,
               "brandcheck": brandcheck,
               "gendercheck" : gendercheck,
               "allcheck" : allcheck,
               "cart": cart}

    return render(request, 'catalog.html', context)


def underconstruction(request):
    return render(request, 'underConstruction.html')


def contact(request):
    return render(request, 'contact.html')

def news(request):
    story = NewS.objects.all()
    context = {
        "story" : story
    }
    return render(request, 'news.html', context)

def article(request):
    return render(request, 'article.html')

def account(request, username=""):
    cart = Cart(request)
    legit = False
    try:
        order = OrderBy.objects.filter(user_ID = request.user.profile)
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
        context = {"form": form,
                   "legit": legit,
                   "users": p,
                   "order": order,
                   "cart": cart, }
        return render(request, 'account.html', context)
    except:
        next = request.POST.get('next', '/home')
        return HttpResponseRedirect(next)


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            u = request.user
            u.profile.pic = form.cleaned_data['image']
            u.save()
            next = request.POST.get('next', '/home')
            return HttpResponseRedirect(next)
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
