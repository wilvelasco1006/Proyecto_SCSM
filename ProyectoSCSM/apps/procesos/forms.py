from django import forms
from django.utils import timezone
from .models import CafeTrillado, CafeTostado, CafeMolido, CafeEmpacado
from datetime import date

class ProcesoBaseForm(forms.ModelForm):
    """Form base para todos los procesos."""
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        # Validar que la fecha no sea futura
        if fecha > date.today():
            raise forms.ValidationError("La fecha no puede ser futura.")
        return fecha
    
    def clean_responsable(self):
        responsable = self.cleaned_data.get('responsable')
        # Validar que el responsable no contenga números
        if any(char.isdigit() for char in responsable):
            raise forms.ValidationError("El nombre del responsable no debe contener números.")
        return responsable

class CafeTrillardoForm(ProcesoBaseForm):
    class Meta:
        model = CafeTrillado
        fields = ['fecha', 'cantidad', 'unidad', 'responsable']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '0.01', 'step': '0.01'}),
            'unidad': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor que cero.")
        return cantidad

class CafeTostadoForm(ProcesoBaseForm):
    class Meta:
        model = CafeTostado
        fields = ['fecha', 'cantidad_baches', 'responsable']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_baches': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'step': '1'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_cantidad_baches(self):
        cantidad = self.cleaned_data.get('cantidad_baches')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad de baches debe ser mayor que cero.")
        return cantidad

class CafeMolidoForm(ProcesoBaseForm):
    class Meta:
        model = CafeMolido
        fields = ['fecha', 'cantidad_baches', 'responsable']
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad_baches': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'step': '1'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_cantidad_baches(self):
        cantidad = self.cleaned_data.get('cantidad_baches')
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad de baches debe ser mayor que cero.")
        return cantidad

class CafeEmpacadoForm(ProcesoBaseForm):
    class Meta:
        model = CafeEmpacado
        fields = [
            'fecha', 'libras_tradicional', 'medias_tradicional', 'cuartos_tradicional',
            'libras_premium', 'medias_premium', 'cuartos_premium', 'responsable'
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'libras_tradicional': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'medias_tradicional': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'cuartos_tradicional': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'libras_premium': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'medias_premium': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'cuartos_premium': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '1'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        # Verificar que al menos un campo de empaque tenga valor
        empaque_fields = [
            'libras_tradicional', 'medias_tradicional', 'cuartos_tradicional',
            'libras_premium', 'medias_premium', 'cuartos_premium'
        ]
        
        if all(cleaned_data.get(field, 0) == 0 for field in empaque_fields):
            raise forms.ValidationError("Debe ingresar al menos una cantidad de café empacado.")
        
        return cleaned_data