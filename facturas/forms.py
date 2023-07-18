from django import forms
from .models import Cliente, Inventario, Factura, DetalleFactura


class ClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class CrearProducto(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'


class FacturaHead(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'


class FacturaDetail(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = '__all__'