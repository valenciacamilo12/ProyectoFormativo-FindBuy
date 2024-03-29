from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Usuario(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}{}'.format(self.user.first_name, self.user.last_name)

    class Meta:
        permissions = {
            ('is_cliente', _('Usuario Cliente')),
        }

