from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse
from django.conf import settings

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
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('home')),
        "cancel_return": request.build_absolute_uri(reverse('home')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, 'cart':cart,}

    return render(request,'detail.html', context)
# Create your views here.
