# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import EditForm, ImageUploadForm, ReviewForm, CommentForm
from .models import Product, Prod4, Prod360, OrderBy, OrderList, Supplier, NewS, Product_Comment, NewS_Comment
from django.contrib.auth.models import User
from register.models import Profile
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from django.views.decorators.http import require_POST
from cart.cart import Cart

import random
import datetime
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
        comment = Product_Comment.objects.filter(product_ID = product_id).order_by('-date')

        if pic_format == 4:
            path = Prod4.objects.all()
        else :
            path = Prod360.objects.all()

        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                Product_Comment.objects.create(product_ID = number, writer = form.cleaned_data.get('writer'), comment = form.cleaned_data.get('comment'), date = datetime.datetime.now())
                next = request.POST.get('next', '/catalog')
                return HttpResponseRedirect(next)
        else:
            form = ReviewForm(request.POST)

        context = {"product": product,
                   "number": number,
                   "path": path,
                   "pic_format": pic_format,
                   "cart_product_form":cart_product_form,
                   "logo_path": logo_path,
                   "logo": logo,
                   "cart": cart,
                   "form": form,
                   "comment": comment,}
        return render(request, 'product.html', context)
    except Exception as e:
        next = request.POST.get('next', '/catalog')
        return HttpResponseRedirect(next)


def catalog(request, product_brand="",key_sort=""):
    cart = Cart(request)
    brandcheck = []
    gendercheck = []
    allcheck = []
    keycheck = []
    brandcheck = request.POST.getlist("radio-set-2")
    gendercheck = request.POST.getlist("radio-set-1")
    allcheck = request.POST.getlist("radio-set-3")
    keycheck = request.POST.get("key")
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



    if key_sort == 'sale' or keycheck == 'sale':
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-promotion')
        keycheck = key_sort
    elif keycheck == 'name':
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-product_Name')
    elif keycheck == 'price':
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-unit_Price_Sale')
    else:
        trueCatalog = catalog.filter(Q(brand__in = brandcheck) & Q(gender__in = gendercheck)).order_by('-product_Name')
        keycheck = 'name'


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
               "keycheck" : keycheck,
               "cart": cart}

    return render(request, 'catalog.html', context)


def underconstruction(request):
    return render(request, 'underConstruction.html')


def contact(request):
    return render(request, 'contact.html')

def news(request):
    cart = Cart(request)
    product = Product.objects.all()
    new = NewS.objects.all().order_by('-date')
    randlist = random.sample(range(new.count()), 6)
    sidenew = []
    for i in randlist:
        s = new[i]
        sidenew.append(s)

    randlist = random.sample(range(new.count()), 3)
    sidenewwithpic = []
    for i in randlist:
        s = new[i]
        sidenewwithpic.append(s)

    story = new[1:]
    firststory = new[:1].get()

    context = {
        "new" : new,
        "story" : story,
        "firststory" : firststory,
        "sidenew" : sidenew,
        "sidenewwithpic" : sidenewwithpic,
        "product": product,
         "cart": cart
    }
    return render(request, 'news.html', context)

def article(request, news_id = ""):
    product = Product.objects.all()
    cart = Cart(request)
    new = NewS.objects.get(news_ID = news_id)
    comment = NewS_Comment.objects.filter(news_ID = news_id).order_by('-date')

    getnew = NewS.objects.all().order_by('-date')
    randlist = random.sample(range(getnew.count()), 6)
    sidenew = []
    for i in randlist:
        s = getnew[i]
        sidenew.append(s)

    randlist = random.sample(range(getnew.count()), 3)
    sidenewwithpic = []
    for i in randlist:
        s = getnew[i]
        sidenewwithpic.append(s)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            NewS_Comment.objects.create(news_ID = new, writer = form.cleaned_data.get('writer'), comment = form.cleaned_data.get('comment'), date = datetime.datetime.now())
            next = request.POST.get('next', '/news')
            return HttpResponseRedirect(next)
        else:
            print("KUY")
    else:
        form = CommentForm(request.POST)
    context = {
        "new": new,
        "getnew" : getnew,
        "form": form,
        "sidenew" : sidenew,
        "sidenewwithpic" : sidenewwithpic,
        "comment": comment,
        "product": product,
        "cart": cart
    }
    return render(request, 'article.html', context)

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
