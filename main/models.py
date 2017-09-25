# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
	product_Name = models.CharField(max_length=75)
	product_Detail = models.CharField(max_length=200)
	product_ID = models.CharField(max_length=45)
	category_ID = models.CharField(max_length=45)
	unit_in_stock = models.IntegerField(default=0)
	unit_Price = models.IntegerField()
	color = models.CharField(max_length=45)

	def __str__(self):
		return self.product_ID

class Size(models.Model):
	product_ID = models.ForeignKey('Product')
	size_06 = models.IntegerField(default=0)
	size_07 = models.IntegerField(default=0)
	size_08 = models.IntegerField(default=0)
	size_09 = models.IntegerField(default=0)
	size_10 = models.IntegerField(default=0)
	size_11 = models.IntegerField(default=0)
	size_12 = models.IntegerField(default=0)
	size_13 = models.IntegerField(default=0)

	def __str__(self):
		return self.product_ID

class Supplier(models.Model):
	supplier_ID = models.ForeignKey('Product')
	company_name = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	phone = models.CharField(max_length=45)
	logo = models.CharField(max_length=45)

	def __str__(self):
		return self.supplier_ID

class Order(models.Model):
	order_ID = models.CharField(max_length=45)
	customer_ID = models.CharField(max_length=45)
	order_Date = models.DateTimeField('date ordered')
	payment_Detail = models.CharField(max_length=45)

	def __str__(self):
		return self.order_ID

class Customer(models.Model):
	customer_ID = models.CharField(max_length=45)
	First_Name = models.CharField(max_length=45)
	Last_Name = models.CharField(max_length=45)
	Address = models.CharField(max_length=45)
	Password = models.CharField(max_length=45)
	History = models.CharField(max_length=45)
	email = models.CharField(max_length=45)
	product_Name = models.CharField(max_length=45)

	def __str__(self):
		return self.customer_ID