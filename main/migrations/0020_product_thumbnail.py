# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20171030_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]