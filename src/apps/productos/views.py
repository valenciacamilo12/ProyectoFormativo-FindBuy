from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from apps.productos.forms import ProductoForm, CategoriaForm, VentaForm
from django.urls import reverse_lazy
from apps.productos.models import Producto, Categoria, Venta, VentaProducto

def index(request):
    return render(request, 'base/base.html')


class Createproducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')


class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')



class DeleteProducto(DeleteView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/productos_delete.html'
    success_url = reverse_lazy('productos:producto_listar')


class ListProduct(ListView):
    model = Producto
    template_name = 'productos/productos_list.html'




#--------------------Categorias---------------------------------------


class ListCategoria(ListView):
    model = Categoria
    template_name = 'productos/productos_list.html'


class UpdateCategoria(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'productos/categorias_list.html'
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