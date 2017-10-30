# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from django import forms
import random
# Create your models here.


class Product(models.Model):
    product_ID = models.CharField(max_length=45, default='', primary_key=True)
    product_Name = models.CharField(max_length=75, default='')
    product_Description = models.CharField(max_length=200, default='')
    gender = models.CharField(max_length=20, default='')
    brand = models.CharField(max_length=45, default='')
    unit_Price = models.IntegerField()
    promotion = models.IntegerField(default=0)
    pic_Format = models.CharField(max_length=3, default='')

    def __str__(self):
        return str(self.product_ID)

    def format(self):
        return int(self.pic_Format)

    def get_brand(self):
        return str(self.brand)


class ProdSize(models.Model):
    product_ID = models.ForeignKey('Product')
    size = models.DecimalField(max_digits=3, decimal_places=1)
    unit = models.IntegerField(default=0)

    def __str__(self):
        return str(self.product_ID)


class Prod4(models.Model):
    product_ID = models.ForeignKey('Product')
    pic1 = models.FileField(null=True, blank=True)
    pic2 = models.FileField(null=True, blank=True)
    pic3 = models.FileField(null=True, blank=True)
    pic4 = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return str(self.product_ID)

    

class Prod360(models.Model):
    product_ID = models.ForeignKey('Product')
    pic1 = models.FileField(null=True, blank=True)
    pic2 = models.FileField(null=True, blank=True)
    pic3 = models.FileField(null=True, blank=True)
    pic4 = models.FileField(null=True, blank=True)
    pic5 = models.FileField(null=True, blank=True)
    pic6 = models.FileField(null=True, blank=True)
    pic7 = models.FileField(null=True, blank=True)
    pic8 = models.FileField(null=True, blank=True)
    pic9 = models.FileField(null=True, blank=True)
    pic10 = models.FileField(null=True, blank=True)
    pic11 = models.FileField(null=True, blank=True)
    pic12 = models.FileField(null=True, blank=True)
    pic13 = models.FileField(null=True, blank=True)
    pic14 = models.FileField(null=True, blank=True)
    pic15 = models.FileField(null=True, blank=True)
    pic16 = models.FileField(null=True, blank=True)
    pic17 = models.FileField(null=True, blank=True)
    pic18 = models.FileField(null=True, blank=True)
    pic19 = models.FileField(null=True, blank=True)
    pic20 = models.FileField(null=True, blank=True)
    pic21 = models.FileField(null=True, blank=True)
    pic22 = models.FileField(null=True, blank=True)
    pic23 = models.FileField(null=True, blank=True)
    pic24 = models.FileField(null=True, blank=True)
    pic25 = models.FileField(null=True, blank=True)
    pic26 = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.product_ID)


class OrderBy(models.Model):
    order_ID = models.CharField(max_length=45)
    user_ID = models.ForeignKey('register.Profile', default='')
    order_Date = models.DateTimeField('date ordered')
    address_to_send = models.CharField(max_length=200)
    date_send = models.DateTimeField('date delivered')

    def __str__(self):
        return str(self.order_ID)


class OrderList(models.Model):
    order_ID = models.ForeignKey('OrderBy')
    product_ID = models.ForeignKey('Product')
    size = models.IntegerField()
    unit = models.IntegerField()

    def __str__(self):
        return str(self.order_ID)


class Supplier(models.Model):
    brand = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return str(self.brand)


class NewS(models.Model):
    news_ID = models.CharField(max_length=45, default='')
    date = models.DateTimeField()
    topic = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=2000, default='')
    pic = models.FileField(null=True, blank=True)
    source = models.CharField(max_length=500, default='')

    def __str__(self):
        return str(self.news_ID)
