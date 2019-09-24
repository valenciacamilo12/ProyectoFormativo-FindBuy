from django.conf.urls import url
from apps.clientes.views import CreateCliente

urlpatterns = [
    url(r'^registro$', CreateCliente.as_view(), name='registro'),
]