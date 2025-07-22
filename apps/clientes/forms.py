from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres', 'apellidos', 'cedula', 'email', 'direccion', 'num_contacto']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Juan'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: Pérez'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'num_contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 3001234567'}),
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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
        if email.count('@') != 1 or email.index('@') < 3:
            raise forms.ValidationError("El email debe contener al menos 3 caracteres antes del '@'.")
        if "." not in email.split("@")[-1]:
            raise forms.ValidationError("Ingrese un email válido.")
        return email

    def clean_direccion(self):
        direccion = self.cleaned_data.get("direccion")
        if len(direccion) < 6:
            raise forms.ValidationError("La dirección debe tener al menos 6 caracteres.")
        if direccion.isdigit():
            raise forms.ValidationError("La dirección no debe contener solo números.")
        return direccion