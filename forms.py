from django import forms


class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    correo = forms.EmailField()
    edad = forms.IntegerField()
    intereses = forms.CharField(max_length=100)


class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)
    precio = forms.FloatField()
    stock = forms.IntegerField()


class CompraFormulario(forms.Form):
    cliente = forms.CharField(max_length=40)
    producto = forms.CharField(max_length=50)
    tienda = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()


class BuscarProductoFormulario(forms.Form):
    categoria = forms.CharField(max_length=50)