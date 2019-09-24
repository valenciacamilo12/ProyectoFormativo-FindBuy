from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from apps.productos.forms import ProductoForm, CategoriaForm, VentaForm, VentaProductoForm
from django.urls import reverse_lazy
from apps.productos.models import Producto as ProductoModel, Categoria, Venta, VentaProducto
from django.http import HttpResponseRedirect

class CreateProducto(CreateView):
    model = ProductoModel
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')


class DetailViewProducto(DetailView):
    model = ProductoModel
    template_name = 'productos/producto_detail.html'

class UpdateProducto(UpdateView):
    model = ProductoModel
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:producto_listar')


class OfertaProducto(ListView):
    model = ProductoModel
    template_name = 'productos/ofertas.html'




# Esto es una Prueba
class Informacion(ListView):
    model = ProductoModel
    template_name = 'informacion/preguntas.html'


class DeleteProducto(DeleteView):
    model = ProductoModel
    form_class = ProductoForm
    template_name = 'productos/producto_delete.html'
    success_url = reverse_lazy('productos:producto_listar')


class ListProducto(ListView):
    model = ProductoModel
    template_name = 'productos/productos_list.html'


def index(request):

    if request.method == "GET":
        try:
            listaProductos = ProductoModel.objects.all()
            return render(request, 'productos/index.html', {'listaProductos': listaProductos})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos xd, lo sentimos."})

    elif request.method == "POST":
        print("Hola entre a post")
        '''
        try:
            
            #listaProductos = ProductoModel.objects.all()
            #return render(request, 'productos/index.html', {'listaProductos': listaProductos})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos xd, lo sentimos."})
        '''


def PorMenosde40(request):

    if request.method == "GET":
        try:
            listaProductos = ProductoModel.objects.filter(precio__lte='40.000')
            return render(request, 'productos/menos40.html', {'listaProductos': listaProductos})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos por menos de 40.000 , lo sentimos."})

    else:
        return render(request, "pages-404.html", {"msg": "Peticion Invalida"})


#--------------------Categorias-------------------------------

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
    template_name = 'productos/tienda_form.html'
    success_url = reverse_lazy('productos:ventaproducto_listar')


class DeleteProductoVenta(DeleteView):
    model = VentaProducto
    form_class = VentaProductoForm
    template_name = 'productos/tienda_delete.html'
    success_url = reverse_lazy('productos:ventaproducto_listar')


class UpdateProductoVenta(UpdateView):
    model = VentaProducto
    form_class = VentaProductoForm
    template_name = 'productos/tienda_form.html'
    success_url = reverse_lazy('productos:ventaproducto_listar')

class ListProductoVenta(ListView):
    model = VentaProducto
    template_name = 'productos/tienda_list.html'

