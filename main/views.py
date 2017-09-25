# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

app_name = 'main'
def home(request):
	return render(request, 'home.html')

def product(request):
	return render(request, 'product.html')