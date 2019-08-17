# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-17 23:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('fecha', models.CharField(max_length=40)),
                ('total', models.CharField(max_length=40)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VentaProducto',
            fields=[
                ('id_ventaproducto', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_venta', models.CharField(max_length=40)),
                ('descuento', models.CharField(max_length=40)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
                ('venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Venta')),
            ],
        ),
    ]
