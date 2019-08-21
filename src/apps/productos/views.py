from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from apps.productos.models import Producto

def index(request):
    return render(request, 'base/base.html')


class Createproducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('productos:productos_listar')

