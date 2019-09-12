from django.conf.urls import url
from apps.productos.views import Producto, ListProducto, CreateProducto, UpdateProducto, DetailViewProducto, DeleteProducto, OfertaProducto, Menos40Producto
from apps.productos.views import ListCategoria, CreateCategoria, UpdateCategoria, DeleteCategoria
from apps.productos.views import ListProductoVenta, CreateProductoVenta, UpdateProductoVenta, DeleteProductoVenta
from apps.productos.views import ListVenta, CreateVenta, UpdateVenta, DeleteVenta

urlpatterns = [
    #Productos
    url(r'^$', Producto.as_view()),
    url(r'^producto/listar$', ListProducto.as_view(), name='producto_listar'),
    url(r'^producto/crear$', CreateProducto.as_view(), name='producto_crear'),
    url(r'^producto/editar/(?P<pk>[\d]+)/$', UpdateProducto.as_view(), name='producto_editar'),
    url(r'^producto/eliminar/(?P<pk>[\d]+)/$', DeleteProducto.as_view(), name='producto_eliminar'),
    url(r'^detalle/(?P<pk>\d+)$', DetailViewProducto.as_view(), name='producto_detalle'),
    url(r'^ofertas$', OfertaProducto.as_view(), name='producto_ofertas'),
    url(r'^menos40$', Menos40Producto.as_view(), name='producto_menos40'),

    #Categorias
    url(r'^categorias/listar$', ListCategoria.as_view(), name='categoria_listar'),
    url(r'^categorias/crear$', CreateCategoria.as_view(), name='categoria_crear'),
    url(r'^categorias/editar/(?P<pk>[\d]+)/$', UpdateCategoria.as_view(), name='categoria_editar'),
    url(r'^categorias/eliminar/(?P<pk>[\d]+)/$', DeleteCategoria.as_view(), name='categoria_eliminar'),

    #Venta Productos
    url(r'^ventaproductos/listar$', ListProductoVenta.as_view(), name='ventaproducto_listar'),
    url(r'^ventaproductos/crear$', CreateProductoVenta.as_view(), name='ventaproducto_crear'),
    url(r'^ventaproductos/editar/(?P<pk>[\d]+)/$', UpdateProductoVenta.as_view(), name='ventaproducto_editar'),
    url(r'^ventaproductos/eliminar/(?P<pk>[\d]+)/$', DeleteProductoVenta.as_view(), name='ventaproducto_eliminar'),


    #Venta
    url(r'^venta/listar$', ListVenta.as_view(), name='venta_listar'),
    url(r'^venta/crear$', CreateVenta.as_view(), name='venta_crear'),
    url(r'^venta/editar/(?P<pk>[\d]+)/$', UpdateVenta.as_view(), name='venta_editar'),
    url(r'^venta/eliminar/(?P<pk>[\d]+)/$', DeleteVenta.as_view(), name='venta_eliminar'),
]