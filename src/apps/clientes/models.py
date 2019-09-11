from django.db import models
from django.contrib.auth.models import User
from apps.tienda.models import Tienda

class Usuario(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}{}'.format(self.user.first_name, self.user.last_name)

