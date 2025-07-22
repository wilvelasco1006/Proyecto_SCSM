from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombres', 'apellidos', 'cedula', 'num_contacto']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: María'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: López'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'num_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 3109876543'}),
        }

    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if any(char.isdigit() for char in nombres):
            raise forms.ValidationError("Los nombres no deben contener números.")
        return nombres

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if any(char.isdigit() for char in apellidos):
            raise forms.ValidationError("Los apellidos no deben contener números.")
        return apellidos

    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        if not cedula.isdigit():
            raise forms.ValidationError("La cédula debe contener solo números positivos.")
        if int(cedula) <= 0 or len(cedula) < 6 or len(cedula) > 10:
            raise forms.ValidationError("La cédula debe ser un valor positivo entre 6 y 10 dígitos.")
        if cedula[0] == '0':
            raise forms.ValidationError("La cédula no puede comenzar con el número 0.")
        return cedula

    def clean_num_contacto(self):
        num_contacto = self.cleaned_data.get("num_contacto")
        if any(char.isalpha() for char in num_contacto):
            raise forms.ValidationError("El número de contacto no debe contener letras.")
        if not num_contacto.isdigit() or int(num_contacto) < 0 or len(num_contacto) < 7 or len(num_contacto) > 15:
            raise forms.ValidationError("El número de contacto debe ser un número positivo entre 7 y 15 dígitos.")
        return num_contacto