# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(OrderBy)
admin.site.register(OrderList)
admin.site.register(Customer)
admin.site.register(OrderTemp)
