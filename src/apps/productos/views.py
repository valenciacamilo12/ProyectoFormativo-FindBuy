from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from apps.productos.forms import ProductoForm, CategoriaForm, VentaForm, VentaProductoForm
from django.urls import reverse_lazy
from apps.productos.models import Producto as ProductoModel, Categoria as CategoriaModel, Venta, VentaProducto
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


def ofertas(request):
    if request.method == "GET":
        try:
            listaProductos = ProductoModel.objects.all()
            listaCategorias = CategoriaModel.objects.all()
            print(listaCategorias)

            return render(request, 'productos/ofertas.html', {'listaProductos': listaProductos, 'listaCategorias': listaCategorias})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos xd, lo sentimos."})




def informacion(request):

    if request.method == "GET":
        try:
            listaCategorias = CategoriaModel.objects.all()

            return render(request, 'productos/informacion.html', {'listaCategorias': listaCategorias})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos xd, lo sentimos."})


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
            listaCategorias = CategoriaModel.objects.all()

            return render(request, 'productos/index.html', {'listaProductos': listaProductos, 'listaCategorias': listaCategorias})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos xd, lo sentimos."})



def categoria(request, idcategoria):

    if request.method == "GET":
        try:
            listaProductos = ProductoModel.objects.filter(categoria=idcategoria)
            listaCategorias = CategoriaModel.objects.all()

            return render(request, 'productos/categoria.html',
                          {'listaProductos': listaProductos, 'listaCategorias': listaCategorias})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos xd, lo sentimos."})


def PorMenosde40(request):

    if request.method == "GET":
        try:
            listaProductos = ProductoModel.objects.filter(precio__lt='40.00')
            listaCategorias = CategoriaModel.objects.all()
            return render(request, 'productos/menos40.html', {'listaProductos': listaProductos ,'listaCategorias': listaCategorias})

        except FileExistsError:
            return render(request, "pages-404.html", {"msg": "No hay productos por menos de 40.000 , lo sentimos."})

    else:
        return render(request, "pages-404.html", {"msg": "Peticion Invalida"})



def Venta(request):
    try:
        #datosProducto = ProductoModel.objects.get(datusuario=request.user.id)

        if request.method == "GET":
            form = VentaForm()
            return render(request, 'productos/venta.html', {'form': form})

        elif request.method == "POST":

            form = VentaForm(request.POST)

            if form.is_valid():
                print("Holaaa")
                form.save()

            form = VentaForm()
            return render(request, "productos/venta.html", {'form': form})

        else:
            return render(request, "pages-404.html", {"msg": "Peticion Invalida"})

    except ProductoModel.DoesNotExist:
        return render(request, "pages-404.html",
                      {"msg": "El Usuario no tiene Datos regidtrados. Comuniquede con el Administrador de Sistema"})





#--------------------Categorias-------------------------------


class ListCategoria(ListView):
    model = CategoriaModel
    template_name = 'productos/categoria_list.html'


class UpdateCategoria(UpdateView):
    model = CategoriaModel
    form_class = CategoriaForm
    template_name = 'productos/categoria_list.html'
    success_url = reverse_lazy('productos:categoria_listar')


class DeleteCategoria(DeleteView):
    model = CategoriaModel
    form_class = CategoriaForm
    template_name = 'productos/categoria_delete.html'
    success_url = reverse_lazy('productos:categoria_listar')


class CreateCategoria(CreateView):
    model = CategoriaModel
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

