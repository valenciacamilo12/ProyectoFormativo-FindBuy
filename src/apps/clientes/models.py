from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.tienda.models import Tienda

class User(AbstractUser):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    nombre_usuario = models.CharField(max_length=40)
    contraseña = models.CharField(max_length=40)
    tienda = models.ForeignKey(Tienda, models.CASCADE, null=True, blank=True)

