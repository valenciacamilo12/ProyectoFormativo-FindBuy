from django.conf.urls import url
from apps.productos.views import index, ListProducto

urlpatterns = [
    url(r'^producto/listar$', ListProducto.as_view(), name='producto_listar'),
]