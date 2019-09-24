from django.shortcuts import render
from apps.clientes.models import User, Usuario
from apps.clientes.forms import RegistroUsuarioForm
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'base/base.html')

class CreateCliente(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'registro.html'
    success_url = reverse_lazy('login')


class UpdateCliente(UpdateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')


class DeleteCliente(DeleteView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente:cliente_listar')

class ListCliente(ListView):
    model = Usuario
    template_name = 'cliente/cliente_list.html'


#------------------------------Info y paginas de ayuda-------------------------

class CentroVendoderes(ListView):
    model = Usuario
    template_name = 'informacion/centroparavendedores.html'


class ComoComprar(ListView):
    model = Usuario
    template_name = 'informacion/comocomprar.html'

class ComoVender(ListView):
    model = Usuario
    template_name = 'informacion/comovender.html'


class Garantia(ListView):
    model = Usuario
    template_name = 'informacion/garantia.html'

class Preguntas(ListView):
    model = Usuario
    template_name = 'informacion/preguntas.html'


class Seguridad(ListView):
    model = Usuario
    template_name = 'informacion/seguridad.html'
