# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import EditForm
from .models import Product
from django.contrib.auth.models import User
from register.models import Profile
from django.http import HttpResponseRedirect
import random
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


def account(request,user_id):
	legit = False
	users = Profile.objects.get(pk=user_id)
	if(users.user.username == request.user.username):
		legit = True

	context = {"users":users,
	"legit":legit}

	return render(request, 'account.html',context)


def catalog(request,gender="",product_brand = ""):
	catalog = Product.objects.all()
	product = Product.objects.all()

	brandlist = []
	brandlist_Object = []
	for i in catalog:
		if not(i.brand in brandlist):
			brandlist.append(i.brand)
			brandlist_Object.append(i)

	if product_brand != "":
		catalog = catalog.filter(brand = product_brand)

	context = {"catalog" : catalog,
				"product": product,
				"brandlist" : brandlist_Object}

	return render(request, 'catalog.html',context)



def underconstruction(request):
	return render(request, 'underConstruction.html')


def contact(request):
	return render(request, 'contact.html')


def edit(request,user_id):
	legit = False
	u = User.objects.get(pk=user_id)
	p = Profile.objects.get(pk=user_id)
	if(u.username == request.user.username):
		legit = True
	if request.method == 'POST':
		form = EditForm(data = request.POST, instance = u)
		if form.is_valid():
			u.username = form.cleaned_data.get('username')
			u.first_name = form.cleaned_data.get('first_name')
			u.last_name = form.cleaned_data.get('last_name')
			u.email = form.cleaned_data.get('email')
			u.profile.address = form.cleaned_data.get('address')
			u.save()
			next = request.POST.get('next', '/home')
			return HttpResponseRedirect(next)
	else:
		form = EditForm(instance = u)

	context = {'form': form ,
				"legit": legit, }
	return render(request, 'edit.html', context)
