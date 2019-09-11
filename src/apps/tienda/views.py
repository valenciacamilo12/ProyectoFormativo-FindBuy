from django.shortcuts import render
from apps.tienda.models import Tienda
from apps.tienda.forms import FormTienda
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

class CreateTienda(CreateView):
    model = Tienda
    form_class = FormTienda
    template_name = 'tienda/tienda_form.html'
    success_url = reverse_lazy('tienda:tienda_listar')


class UpdateTienda(UpdateView):
    model = Tienda
    form_class = FormTienda
    template_name = 'tienda/tienda_form.html'
    success_url = reverse_lazy('tienda:tienda_listar')


class DeleteTienda(DeleteView):
    model = Tienda
    form_class = FormTienda
    template_name = 'tienda/tienda_delete.html'
    success_url = reverse_lazy('tienda:tienda_listar')


class ListTienda(ListView):
    model = Tienda
    template_name = 'tienda/tienda_list.html'
