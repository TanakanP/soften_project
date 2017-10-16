from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

from main.models import Product

def checkout(request,product_id):
    # product = Product.get
    product = Product.objects.all()
    number = Product.objects.get(pk=product_id)
    # What you want the button to do.
    paypal_dict = {
        "business": "sassneaker@gmail.com",
        "amount": number.unit_Price,
        "item_name": number.product_Name,
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('home')),
        "cancel_return": request.build_absolute_uri(reverse('home')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form,
                "product": product,
                "number": number}

    return render(request, "payment.html", context)
