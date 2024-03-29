# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-29 06:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.FloatField(max_length=40)),
                ('foto', models.ImageField(height_field='height_field', upload_to='', width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('existencias', models.IntegerField()),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=datetime.datetime.now, null=True)),
                ('total', models.CharField(default=True, max_length=40, null=True)),
                ('firstname_cliente', models.CharField(max_length=40)),
                ('lastname_cliente', models.CharField(max_length=40)),
                ('pais_cliente', models.CharField(max_length=40)),
                ('direccion_cliente', models.CharField(max_length=40)),
                ('ciudad_cliente', models.CharField(max_length=40)),
                ('telefono_cliente', models.CharField(max_length=40)),
                ('correo_cliente', models.CharField(max_length=40)),
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
