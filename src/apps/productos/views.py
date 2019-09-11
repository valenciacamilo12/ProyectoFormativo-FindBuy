from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from apps.productos.forms import ProductoForm, CategoriaForm, VentaForm, VentaProductoForm
from django.urls import reverse_lazy
from apps.productos.models import Producto, Categoria, Venta, VentaProducto

def index(request):
    return render(request, 'base/base.html')


class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')


class DetailViewProducto(DetailView):
    model = Producto
    template_name = 'productos/producto_detail.html'

class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class DeleteProducto(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_delete.html'
    success_url = reverse_lazy('productos:producto_listar')


# esto es un codigo de prueba
class ListProducto(ListView):
    model = Producto
    template_name = 'productos/productos_list.html'

class Producto(ListView):
    model = Producto
    template_name = 'productos/index.html'




#--------------------Categorias---------------------------------------


class ListCategoria(ListView):
    model = Categoria
    template_name = 'productos/categoria_list.html'


class UpdateCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categoria_list.html'
    success_url = reverse_lazy('productos:categoria_listar')


class DeleteCategoria(DeleteView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categoria_delete.html'
    success_url = reverse_lazy('productos:categoria_listar')


class CreateCategoria(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categoria_form.html'
    success_url = reverse_lazy('productos:categoria_listar')



#---------------------------Venta----------------------------

class CreateVenta(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'productos/venta_form.html'
    success_url = reverse_lazy('productos:venta_listar')


class DeleteVenta(DeleteView):
    model = Venta
    form_class = VentaForm
    template_name = 'productos/venta_delete.html'
    success_url = reverse_lazy('productos:ventas_listar')


class UpdateVenta(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'productos/venta_form.html'
    success_url = reverse_lazy('productos:ventas_listar')

class ListVenta(ListView):
    model = Venta
    template_name = 'productos/venta_list.html'




#----------------------------Venta Producto--------------------

class CreateProductoVenta(CreateView):
    model = VentaProducto
    form_class = VentaProductoForm
    template_name = 'productos/ventaproducto_form.html'
    success_url = reverse_lazy('productos:ventaproducto_listar')


class DeleteProductoVenta(DeleteView):
    model = VentaProducto
    form_class = VentaProductoForm
    template_name = 'productos/ventaproducto_delete.html'
    success_url = reverse_lazy('productos:ventaproducto_listar')


class UpdateProductoVenta(UpdateView):
    model = VentaProducto
    form_class = VentaProductoForm
    template_name = 'productos/ventaproducto_form.html'
    success_url = reverse_lazy('productos:ventaproducto_listar')

class ListProductoVenta(ListView):
    model = VentaProducto
    template_name = 'productos/ventaproducto_list.html'

