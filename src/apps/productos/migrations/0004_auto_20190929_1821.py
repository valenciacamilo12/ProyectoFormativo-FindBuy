# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-29 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_auto_20190929_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='id_producto',
            field=models.CharField(default=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_cliente',
            field=models.CharField(max_length=40),
        ),
    ]
