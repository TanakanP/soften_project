# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product

# Create your views here.

app_name = 'main'
def home(request):
	product = Product.objects.all()
	return render(request, 'home.html',{"product":product})

def product(request,product_id):
	product = Product.objects.all()
	number = Product.objects.get(pk=product_id)
	context = {"product":product,
				"number":number}
	return render(request, 'product.html',context)

def catalog(request):
	catalog = Product.objects.all()
	product = Product.objects.all()
	context = {"catalog" : catalog,
				"product": product}
	return render(request, 'catalog.html',context)

def underconstruction(request):
	return render(request, 'underConstruction.html')