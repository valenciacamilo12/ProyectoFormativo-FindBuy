from django.conf.urls import url
from apps.tienda.views import registroTienda, UpdateTienda, DeleteTienda, ListTienda

urlpatterns = [
    url(r'^listar$', ListTienda.as_view(), name='tienda_listar'),
    url(r'^crear/(?P<pk>[\d]+)/$', registroTienda, name='tienda_crear'),
    url(r'^editar/(?P<pk>[\d]+)/$', UpdateTienda.as_view(), name='tienda_editar'),
    url(r'^eliminar/(?P<pk>[\d]+)/$', DeleteTienda.as_view(), name='tienda_eliminar'),
]