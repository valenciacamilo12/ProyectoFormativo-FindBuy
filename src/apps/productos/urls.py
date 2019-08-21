from django.conf.urls import url
from apps.productos.views import index

urlpatterns = [
    url(r'^$', index)
]