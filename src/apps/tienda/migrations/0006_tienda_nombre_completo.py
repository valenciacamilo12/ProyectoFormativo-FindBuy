# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-27 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_auto_20190927_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='tienda',
            name='nombre_completo',
            field=models.CharField(default=True, max_length=40),
        ),
    ]
