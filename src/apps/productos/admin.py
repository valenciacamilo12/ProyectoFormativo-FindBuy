from django.contrib import admin
from apps.productos.models import Venta, VentaProducto, Producto, Categoria
admin.site.register(Venta)
admin.site.register(VentaProducto)
admin.site.register(Producto)
admin.site.register(Categoria)