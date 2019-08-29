from apps.tienda.models import Tienda
from django import forms

class FormTienda(forms.ModelForm):
    class Meta:
        model = Tienda

        fields = "__all__"

        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
        }

    def __init__(self, *args, **kwargs):
        super(FormTienda, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})