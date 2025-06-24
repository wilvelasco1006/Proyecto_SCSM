from django import forms
from .models import Venta, DetalleVenta
from apps.clientes.models import Cliente
from datetime import date

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'fecha', 'responsable']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control', 'id': 'id_cliente'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    # Inicializar fecha con la fecha actual
    def __init__(self, *args, **kwargs):
        super(VentaForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].initial = date.today()
        
        # Mostrar nombre completo de los clientes en el select
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.nombres} {obj.apellidos} (CC: {obj.cedula})"

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['tipo_cafe', 'cantidad', 'precio_unitario']
        widgets = {
            'tipo_cafe': forms.Select(attrs={'class': 'form-control tipo-cafe'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control cantidad', 'min': '1', 'step': '1'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control precio', 'min': '1000', 'step': '100'}),
        }

# Formulario para la creación inicial con un detalle
class VentaConDetalleForm(forms.Form):
    # Campos de la venta
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.filter(is_active=True),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_cliente'})
    )
    direccion_cliente = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        required=False
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        initial=date.today
    )
    responsable = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    # Campos del primer detalle
    tipo_cafe = forms.ChoiceField(
        choices=DetalleVenta.TIPO_CAFE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control tipo-cafe'})
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control cantidad', 'min': '1', 'step': '1'})
    )
    precio_unitario = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control precio', 'min': '1000', 'step': '100'})
    )
    
    def __init__(self, *args, **kwargs):
        super(VentaConDetalleForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.nombres} {obj.apellidos} (CC: {obj.cedula})"