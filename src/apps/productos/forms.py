from apps.productos.models import Producto
from apps.productos.models import Categoria
from apps.productos.models import Venta
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'nombre',
            'precio',
            'foto',
            'existencias',
            'tienda',
            'categoria',
        ]

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'foto': 'Foto',
            'existencias': 'Existencias',
            'tienda': 'Tienda',
            'categoria': 'Categoria',

        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'existencias': forms.TextInput(attrs={'class': 'form-control'}),
            'tienda': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }




class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

        fields = [
            'nombre',
        ]

        labels = {
            'nombre':'Nombre',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
        }


class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta

        fields = [
            'codigo',
            'fecha',
            'total',
            'cliente',
        ]

        labels = {
            'codigo':'Codigo',
            'fecha':'Fecha',
            'total':'Total',
            'cliente':'Cliente',
        }

        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class':'form-control'}),
            'total': forms.TextInput(attrs={'class':'form-control'}),
            'cliente': forms.Select(attrs={'class':'form-control'}),
        }