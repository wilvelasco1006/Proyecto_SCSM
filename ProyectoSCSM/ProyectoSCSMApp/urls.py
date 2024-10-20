
from django.urls import path
from . views import home,ingresar,exit, register

# Definición de las rutas URL para la aplicación
urlpatterns = [
    path('', home, name='home'), # Ruta principal
    path('ingresar/', ingresar, name='ingresar'), #Ruta para ingresar al sistema
    path('logout/', exit, name= 'exit'), #Ruta para cerrar la sesion
    path('register/', register, name= 'register'), #Ruta para registrarse

]