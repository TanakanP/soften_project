# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170926_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]