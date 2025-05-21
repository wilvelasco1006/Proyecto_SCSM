from django import forms
from .models import Cafe
from datetime import date
class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['fecha_compra', 'cantidad', 'precio', 'datos_proveedor']
        # Obtener la fecha de hoy en formato string para los atributos min y max
        today_str = date.today().strftime('%Y-%m-%d')
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date','min': today_str, 'max': today_str,}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 30000'}),
            'datos_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser un valor positivo mayor a 0.")
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return precio
    def __init__(self, *args, **kwargs):
        super(CafeForm, self).__init__(*args, **kwargs)
        # Establecer la fecha actual como valor predeterminado
        self.initial['fecha_compra'] = date.today()
    
    def clean_fecha_compra(self):
        fecha = self.cleaned_data['fecha_compra']
        # Validar que la fecha sea hoy
        if fecha != date.today():
            raise forms.ValidationError("La fecha debe ser la actual (hoy).")
        return fecha