from apps.productos.models import Producto, Categoria, Venta, VentaProducto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = [
            'id_cliente',
            'nombre',
            'precio',
            'foto',
            'existencias',
            'categoria',
        ]

        labels = {
            'id_cliente': 'Id Cliente',
            'nombre': 'Nombre',
            'precio': 'Precio',
            'foto': 'Foto',
            'existencias': 'Existencias',
            'categoria': 'Categoria',

        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['id_cliente'].widget = forms.HiddenInput()
        self.fields['nombre'].widget.attrs.update({'placeholder': 'Digite el Nombre Del Producto'})
        self.fields['precio'].widget.attrs.update({'placeholder': 'Digite el Precio Del Producto'})
        self.fields['existencias'].widget.attrs.update({'placeholder': 'Digite las Existencias Del Producto'})
        self.fields['categoria'].widget.attrs.update({'placeholder': 'Digite la Categoria Del Producto'})

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})



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
            'id_producto',
            'id_tienda',
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
            'id_producto': 'Id Producto',
            'id_tienda': 'Id Tienda',
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
        self.fields['fecha'].widget = forms.HiddenInput()
        self.fields['total'].widget = forms.HiddenInput()
        self.fields['id_producto'].widget = forms.HiddenInput()
        self.fields['id_tienda'].widget = forms.HiddenInput()
        self.fields['firstname_cliente'].widget.attrs.update({'placeholder': 'Digite sus Nombres'})
        self.fields['lastname_cliente'].widget.attrs.update({'placeholder': 'Digite su Apellidos'})
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
