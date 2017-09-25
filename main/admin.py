# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, Size, Supplier, Order, Customer

# Register your models here.

admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Customer)