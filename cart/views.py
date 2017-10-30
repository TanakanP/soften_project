from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product, OrderBy, OrderList, ProdSize
from .cart import Cart
from .forms import CartAddProductForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse
from django.conf import settings
import datetime

@require_POST
def cart_add(request, product_id):
    cart =Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'],
                size=cd['size'])
    return HttpResponse(status=204)

def cart_sub(request, product_id):
    cart =Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.sub(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'],
                size=cd['size'])
    return HttpResponse(status=204)

def cart_remove(request, product_p):
    cart = Cart(request)
    # product = get_object_or_404(Product,id=product_id)
    cart.remove(product_p)
    return HttpResponse(status=204)
##
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                initial={'quantity':item['quantity'],
                                'update': True,'size':item['size']})

    for i in cart:
        print(i['size'])
        p = Product.objects.get(pk=i['pk'])
        #print(p.__dict__["size_06"])
        #print(p.product_id)

    # What you want the tton to do.kuy
    paypal_dict = {
        "business": "sassneaker@gmail.com",
        "amount": cart.get_total_price(),
        "item_name": "cart",
        "invoice": request.user.id + cart.get_total_price(),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri('order'),
        "cancel_return": request.build_absolute_uri(reverse('home')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, 'cart':cart,}

    return render(request,'detail.html', context)
# Create your views here.

def order(request):
    cart = Cart(request)
    orde = OrderBy.objects.create(user_ID = request.user.profile, order_Date = datetime.datetime.now(), address_to_send = request.user.profile.address, date_send = None)
    for i in cart:
        p = Product.objects.get(pk=i['pk'])
        prod = ProdSize.objects.get(product_ID=i['pk'], size=float(i['size']))
        print(prod.product_ID)
        print(prod.size)
        print(prod.unit)
        prod.unit -= i['quantity']
        prod.save()
        print(prod.unit)
        OrderList.objects.create(order_ID = orde, product_ID = p, size = float(i['size']), unit = i['quantity'])
    return render(request,'detail.html')
