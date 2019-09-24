"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.productos.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete, logout_then_login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^productos/', include('apps.productos.urls', namespace='productos')),
    url(r'^tiendas/', include('apps.tienda.urls', namespace='tienda')),
    url(r'^clientes/', include('apps.clientes.urls', namespace='cliente')),
    url(r'^$', index),
    url(r'^accounts/login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'reset/password_reset', password_reset,
        {'template_name':'registration/password_reset_form.html',
         'email_template_name': 'registration/password_reset_email.html'},
        name='password_reset'),
    url(r'reset_password_done', password_reset_done,
        {'template_name':'registration/password_reset_done.html'},
        name = 'password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-Za-z_ \-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name':'registration/password_reset_confirm.html'},
        name = 'password_reset_confirm'),

    url(r'reset/done', password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name = 'password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)