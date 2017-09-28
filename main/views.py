# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product

# Create your views here.

app_name = 'main'
def home(request):
	product = Product.objects.all()
	return render(request, 'home.html',{"product":product})

def product(request):
	product = Product.objects.all()
	return render(request, 'product.html',{"product":product})

def catalog(request):
	return render(request, 'catalog.html')