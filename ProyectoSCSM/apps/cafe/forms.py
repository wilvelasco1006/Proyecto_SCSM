from django import forms
from .models import Cafe

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['fecha_compra', 'cantidad', 'precio', 'datos_proveedor']
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
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