from django.shortcuts import render
from apps.tienda.models import Tienda
from apps.clientes.models import Usuario as UsuarioModel
from django.contrib.auth.models import User
from apps.tienda.forms import RegistroTiendaForm
from django.views.generic import CreateView, DeleteView,UpdateView,ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def registroTienda(request, pk):

    try:
        datosCliente = User.objects.get(id=pk)

        if request.method == "GET":
            form = RegistroTiendaForm
            return render(request, 'tienda/registro_tienda.html', {'form': form, 'datosCliente': datosCliente})

        elif request.method == "POST":
            form = RegistroTiendaForm(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect(reverse('productos:inicio'))
        else:
            return render(request, "pages-404.html", {"msg": "Peticion Invalida"})



    except Tienda.DoesNotExist:
        return render(request, "pages-404.html", {"msg": "El Usuario no tiene Datos registrados. Comuniquede con el Administrador de Sistema"})


class UpdateTienda(UpdateView):
    model = Tienda
    form_class = RegistroTiendaForm
    template_name = 'tienda/tienda_form.html'
    success_url = reverse_lazy('tienda:tienda_listar')


class DeleteTienda(DeleteView):
    model = Tienda
    form_class = RegistroTiendaForm
    template_name = 'tienda/tienda_delete.html'
    success_url = reverse_lazy('tienda:tienda_listar')


class ListTienda(ListView):
    model = Tienda
    template_name = 'tienda/tienda_list.html'
