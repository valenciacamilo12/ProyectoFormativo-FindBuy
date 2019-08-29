from django.shortcuts import render
from apps.clientes.models import User
from apps.clientes.forms import  FormCliente
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy

def index(request):
    return render(request, 'base/base.html')

class CreateCliente(CreateView):
    model = User
    form_class = FormCliente
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')


class UpdateCliente(UpdateView):
    model = User
    form_class = FormCliente
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')


class DeleteCliente(DeleteView):
    model = User
    form_class = FormCliente
    template_name = 'cliente/cliente_delete.html'
    success_url = reverse_lazy('cliente:cliente_listar')

class ListCliente(ListView):
    model = User
    template_name = 'cliente/cliente_list.html'