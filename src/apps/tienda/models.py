from django.db import models
from django.utils.translation import ugettext as _

class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    id_usuario = models.CharField(max_length=40, default=True)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    nombre_completo = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        permissions = {
            ('is_tienda', _('Usuario Tienda')),
        }

