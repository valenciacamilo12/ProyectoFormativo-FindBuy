from django.conf.urls import url
from apps.clientes.views import CreateCliente, CentroVendoderes, ComoComprar, ComoVender, Garantia, Preguntas, Seguridad

urlpatterns = [
    url(r'^registro$', CreateCliente.as_view(), name='registro'),
    url(r'^centrovendoderes$', CentroVendoderes.as_view(), name='centrovendoderes'),
    url(r'^comocomprar$', ComoComprar.as_view(), name='comocomprar'),
    url(r'^comovender$', ComoVender.as_view(), name='comovender'),
    url(r'^garantia$', Garantia.as_view(), name='garantia'),
    url(r'^preguntas$', Preguntas.as_view(), name='preguntas'),
    url(r'^seguridad$', Seguridad.as_view(), name='seguridad'),
]