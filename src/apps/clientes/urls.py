from django.conf.urls import url
from apps.clientes.views import index

urlpatterns = [
    url(r'^$', index)
]