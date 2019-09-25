from apps.productos.models import Producto, Categoria, Venta, VentaProducto
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
            'fecha',
            'total',
            'firstname_cliente',
            'lastname_cliente',
            'pais_cliente',
            'direccion_cliente',
            'ciudad_cliente',
            'telefono_cliente',
            'correo_cliente',
        ]

        labels = {
            'fecha': 'Fecha',
            'total': 'Total',
            'firstname_cliente':'Nombres',
            'lastname_cliente':'Apellidos',
            'pais_cliente':'Pais',
            'direccion_cliente':'Direccion',
            'ciudad_cliente':'Ciudad',
            'telefono_cliente':'Telefono',
            'correo_cliente':'Correo',
        }

    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['firstname_cliente'].widget.attrs.update({'placeholder': 'Digite sus nombres'})
        self.fields['lastname_cliente'].widget.attrs.update({'placeholder': 'Digite sus apellidos'})
        self.fields['pais_cliente'].widget.attrs.update({'placeholder': 'Digite su Pais'})
        self.fields['direccion_cliente'].widget.attrs.update({'placeholder': 'Digite su Direccion'})
        self.fields['ciudad_cliente'].widget.attrs.update({'placeholder': 'Digite su Ciudad'})
        self.fields['telefono_cliente'].widget.attrs.update({'placeholder': 'Digite su Telefono'})
        self.fields['correo_cliente'].widget.attrs.update({'placeholder': 'Digite su Correo'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class VentaProductoForm(forms.ModelForm):
    class Meta:
        model = VentaProducto

        fields = [
            'cantidad',
            'precio_venta',
            'descuento',
            'producto',
            'venta',
        ]

        labels = {
            'cantidad': 'Cantidad',
            'precio_venta': 'Precio',
            'descuento': 'Descuento',
            'producto': 'Producto',
            'venta': 'Venta',
        }

    def __init__(self, *args, **kwargs):
        super(VentaProductoForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
