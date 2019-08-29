from django import forms
from apps.clientes.models import User

class FormCliente(forms.ModelForm):
    class Meta:
        model = User

        fields = "__all__"

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'nombre_usuario': 'Nombre Usuario',
            'contrasena': 'Contraseña',
            'tienda': 'Tienda',
        }


    def __init__(self, *args, **kwargs):
        super(FormCliente, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})