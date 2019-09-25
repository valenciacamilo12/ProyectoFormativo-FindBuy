from django.db import models
from apps.tienda.models import Tienda
from apps.clientes.models import User
from datetime import datetime

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    precio = models.CharField(max_length=40)
    foto = models.ImageField(blank=True, width_field='width_field', height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    existencias = models.IntegerField()
    tienda = models.ForeignKey(Tienda, models.CASCADE, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha = models.DateField(default=datetime.now)
    total = models.CharField(max_length=40)
    firstname_cliente = models.CharField(max_length=40, default=True)
    lastname_cliente = models.CharField(max_length=40, default=True)
    pais_cliente = models.CharField(max_length=40)
    direccion_cliente = models.CharField(max_length=40)
    ciudad_cliente = models.CharField(max_length=40)
    telefono_cliente = models.CharField(max_length=40)
    correo_cliente = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.id_venta)


class VentaProducto(models.Model):
    id_ventaproducto = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    precio_venta = models.CharField(max_length=40)
    descuento = models.CharField(max_length=40)
    producto = models.ForeignKey(Producto, models.CASCADE, blank=True, null=True)
    venta = models.ForeignKey(Venta, models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.id_ventaproducto)