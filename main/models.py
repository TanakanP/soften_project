# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django import forms

# Create your models here.
class Product(models.Model):
	product_ID = models.CharField(max_length=45,default='')
	product_Name = models.CharField(max_length=75,default='')
	product_Description = models.CharField(max_length=200,default='')
	gender = forms.ChoiceField(choices=[('Male','Male'),
										('Female','Female'),
										('All','All')])
	brand = models.CharField(max_length=45,default='')
	color = models.CharField(max_length=45,default='')
	unit_Price = models.IntegerField()
	picture = models.CharField(max_length=200,default='')
	weight = models.IntegerField(default=0)
	size_06 = models.IntegerField(default=0)
	size_06_5 = models.IntegerField(default=0)
	size_07 = models.IntegerField(default=0)
	size_07_5 = models.IntegerField(default=0)
	size_08 = models.IntegerField(default=0)
	size_08_5 = models.IntegerField(default=0)
	size_09 = models.IntegerField(default=0)
	size_09_5 = models.IntegerField(default=0)
	size_10 = models.IntegerField(default=0)
	size_10_5 = models.IntegerField(default=0)
	size_11 = models.IntegerField(default=0)
	size_11_5 = models.IntegerField(default=0)
	size_12 = models.IntegerField(default=0)
	size_12_5 = models.IntegerField(default=0)
	size_13 = models.IntegerField(default=0)
	size_13_5 = models.IntegerField(default=0)

	def __str__(self):
		return self.product_ID

class Supplier(models.Model):
	brand = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	phone = models.CharField(max_length=45)
	logo = models.CharField(max_length=200)

	def __str__(self):
		return self.brand

class OrderBy(models.Model):
	order_ID = models.CharField(max_length=45)
	customer_ID = models.ForeignKey('Customer')
	order_Date = models.DateTimeField('date ordered')
	address_to_send = models.CharField(max_length=200)
	paid = models.BooleanField()
	date_send = models.DateTimeField('date delivered')

	def __str__(self):
		return self.order_ID

class OrderList(models.Model):
	order_ID = models.ForeignKey('OrderBy')
	product_ID = models.ForeignKey('Product')
	size = models.IntegerField()
	unit = models.IntegerField()

	def __str__(self):
		return str(self.order_ID)

class Customer(models.Model):
	customer_ID = models.CharField(max_length=45)
	First_Name = models.CharField(max_length=45)
	Last_Name = models.CharField(max_length=45)
	Address = models.CharField(max_length=45)
	Password = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	stripe_key = models.CharField(max_length=45)

	def __str__(self):
		return self.customer_ID

class OrderTemp(models.Model):
	customer_ID = models.ForeignKey('Customer')
	order_ID = models.ForeignKey('OrderBy')
	product_ID = models.ForeignKey('Product')
	size = models.IntegerField()
	unit = models.IntegerField()

	def __str__(self):
		return str(self.customer_ID)