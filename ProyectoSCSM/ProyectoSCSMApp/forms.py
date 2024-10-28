from django import forms
# Importa el módulo de formularios de Django, que proporciona las clases base para crear formularios HTML en Django.

from django.contrib.auth.forms import UserCreationForm
# Importa el formulario prediseñado por Django para la creación de usuarios. Este formulario maneja la lógica
# de validación y guardado de un nuevo usuario en la base de datos, incluyendo la gestión de contraseñas.

from django.contrib.auth.models import User
# Importa la clase User del módulo de autenticación de Django. Esta es la clase que Django utiliza por defecto
# para manejar los usuarios registrados en el sistema. Contiene atributos como 'username', 'email', 'password', etc.
from .models import Proveedor,Cafe  #importamos la clas clases que necsitamos

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Especifica que el formulario se basa en el modelo User de Django.
        fields = ['username','first_name', 'last_name', 'email','password1','password2']  
        # Define los campos del formulario que se mostrarán y serán utilizados para crear un usuario.

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'cedula', 'num_contacto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'num_contacto': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['fecha_compra', 'cantidad', 'precio', 'datos_proveedor']
        widgets = {
            'fecha_compra': forms.DateInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'datos_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }
    #funcion para validar que en el formulario no admita negativos en el campo cantidad
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get("cantidad")
        if cantidad<=0:
            raise forms.ValidationError("La cantidad debe ser una valor positivo")
        return cantidad
        
    # Funcion para que no admita negativos en el campo precio
    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio<=0:
            raise forms.ValidationError("El precio debe ser un valor positivo")
        return precio