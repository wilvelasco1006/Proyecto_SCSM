from django import forms
# Importa el módulo de formularios de Django, que proporciona las clases base para crear formularios HTML en Django.

from django.contrib.auth.forms import UserCreationForm
# Importa el formulario prediseñado por Django para la creación de usuarios. Este formulario maneja la lógica
# de validación y guardado de un nuevo usuario en la base de datos, incluyendo la gestión de contraseñas.

from django.contrib.auth.models import User
# Importa la clase User del módulo de autenticación de Django. Esta es la clase que Django utiliza por defecto
# para manejar los usuarios registrados en el sistema. Contiene atributos como 'username', 'email', 'password', etc.
from .models import Proveedor,Cafe, Cliente #importamos la clas clases que necsitamos
import locale
from decimal import Decimal, InvalidOperation
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Especifica que el formulario se basa en el modelo User de Django.
        fields = ['username','first_name', 'last_name', 'email','password1','password2']  
        # Define los campos del formulario que se mostrarán y serán utilizados para crear un usuario.

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombres','apellidos', 'cedula', 'num_contacto']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'tu segundo nombre es opcional'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control','placeholder': 'tu segundo apellido es opcional'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'num_contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }
    # Función para validar que el nombre no sea un número
    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if any(char.isdigit() for char in nombres):
            raise forms.ValidationError("Los nombres no deben contener números.")
        return nombres
    # Validación para que los apellidos no contengan números
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if any(char.isdigit() for char in apellidos):
            raise forms.ValidationError("Los apellidos no deben contener números.")
        return apellidos

    # Función para que la cédula sea un valor positivo
    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        if not cedula.isdigit():
            raise forms.ValidationError("La cédula debe contener solo números positivos.")
        if int(cedula) <= 0 or len(cedula) < 6 or len(cedula) > 10:
            raise forms.ValidationError("La cédula debe ser un valor positivo entre 6 y 10 dígitos.")
        if cedula[0] == '0':
            raise forms.ValidationError("La cédula no puede comenzar con el número 0.")
        return cedula


    # Función para que el número de contacto no contenga letras y no sea negativo
    def clean_num_contacto(self):
        num_contacto = self.cleaned_data.get("num_contacto")
        if any(char.isalpha() for char in num_contacto):
            raise forms.ValidationError("El número de contacto no debe contener letras.")
        if not num_contacto.isdigit() or int(num_contacto) < 0 or len(num_contacto) < 7 or len(num_contacto) > 15:
            raise forms.ValidationError("El número de contacto debe ser un número positivo entre 7 y 15 dígitos.")
        return num_contacto



class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['fecha_compra', 'cantidad', 'precio', 'datos_proveedor']
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '000000'}),
            'datos_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }
    #funcion para validar que en el formulario no admita negativos en el campo cantidad
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        if cantidad<=0:
            raise forms.ValidationError("La cantidad debe ser una valor positivo mayor a 0")
        return cantidad
    
    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        try:
        # Convertir precio a entero
            precio_int = int(precio)
            if precio_int <= 0:
                raise forms.ValidationError("El precio debe ser un valor entero positivo.")
        except ValueError:
            raise forms.ValidationError("Por favor, ingrese un número válido sin puntos ni comas.")
    
    # Devuelve el valor limpio como 'precio' en lugar de 'precio_int' para mantener consistencia
        return precio_int

        
    
    
# Formulario para el cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombres','apellidos', 'cedula', 'email', 'direccion', 'num_contacto']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder': 'tu segundo nombre es opcional'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control','placeholder': 'tu segundo apellido es opcional'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'num_contacto': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    # Validación para que el nombre no contenga números
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

    # Validación para que la cédula sea un valor positivo y no contenga letras
    def clean_cedula(self):
        cedula = self.cleaned_data.get("cedula")
        if not cedula.isdigit():
            raise forms.ValidationError("La cédula debe contener solo números positivos y sin letras.")
        if int(cedula) <= 0 or len(cedula) < 6 or len(cedula) > 10:
            raise forms.ValidationError("La cédula debe ser un valor positivo entre 6 y 10 dígitos.")
        if cedula[0] == '0':
            raise forms.ValidationError("La cédula no puede comenzar con el número 0.")
        return cedula


    # Validación para que el número de contacto no contenga letras y sea positivo
    def clean_num_contacto(self):
        num_contacto = self.cleaned_data.get("num_contacto")
        if any(char.isalpha() for char in num_contacto):
            raise forms.ValidationError("El número de contacto no debe contener letras.")
        if not num_contacto.isdigit() or int(num_contacto) < 0 or len(num_contacto) < 7 or len(num_contacto) > 15:
            raise forms.ValidationError("El número de contacto debe ser un número positivo entre 7 y 15 dígitos.")
        return num_contacto

    # Validación para que el email tenga una estructura válida
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("El email es obligatorio.")
    
    # Verifica que haya al menos 3 caracteres antes del '@'
        if email.count('@') != 1 or email.index('@') < 3:
            raise forms.ValidationError("El email debe contener al menos 3 caracteres antes del '@'.")
    
    # Verifica que haya un dominio después del '@'
        if "." not in email.split("@")[-1]:
            raise forms.ValidationError("Ingrese un email válido.")
    
        return email

    # Validación para que la dirección tenga una longitud mínima y no sea solo números
    def clean_direccion(self):
        direccion = self.cleaned_data.get("direccion")
        if len(direccion) < 6:
            raise forms.ValidationError("La dirección debe tener al menos 6 caracteres.")
        if direccion.isdigit():
            raise forms.ValidationError("La dirección no debe contener solo números.")
        return direccion