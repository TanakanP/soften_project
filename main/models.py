# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	product_Name = models.CharField(max_length=75)
	product_Detail = models.CharField(max_length=200)
	product_ID = models.IntegerField()
	category_ID = models.CharField(max_length=45)
	unit_in_stock = models.IntegerField()
	unit_Price = models.IntegerField()
	color = models.CharField(max_length=45)

	class Meta:
		verbose_name_plural = 'products'

	def __str__(self):
		return self.product_id

