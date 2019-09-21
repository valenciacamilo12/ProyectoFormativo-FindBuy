from django.db import models

class Tienda(models.Model):
    id_tienda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)
