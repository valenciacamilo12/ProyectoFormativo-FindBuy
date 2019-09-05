from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.tienda.models import Tienda

class User(AbstractUser):
    id_cliente = models.AutoField(primary_key=True)
    tienda = models.ForeignKey(Tienda, models.CASCADE, null=True, blank=True)

