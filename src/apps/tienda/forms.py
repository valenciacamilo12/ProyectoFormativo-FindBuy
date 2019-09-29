from apps.tienda.models import Tienda
from django import forms

class RegistroTiendaForm(forms.ModelForm):

    class Meta:
        model = Tienda

        fields = [
            'id_usuario',
            'nombre',
            'direccion',
            'telefono',
            'nombre_completo',
        ]

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'nombre_completo': 'Nombre Completo',
        }

    def __init__(self, *args, **kwargs):
        super(RegistroTiendaForm, self).__init__(*args, **kwargs)
        self.fields['id_usuario'].widget = forms.HiddenInput()
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Digite el nombre de su tienda'})
        self.fields['direccion'].widget.attrs.update({'placeholder': 'Digite la direccion de la tienda'})
        self.fields['telefono'].widget.attrs.update({'placeholder': 'Digite el telefono'})
        self.fields['nombre_completo'].widget.attrs.update({'placeholder': 'Digite el nombre completo del encargado'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
