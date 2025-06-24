"""
URL configuration for ProyectoSCSM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Definición de las rutas URL para la aplicación
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', include('apps.base.urls')),  # Ruta para la página de inicio (home)
    path('clientes/', include('apps.clientes.urls')),  # Rutas de la app clientes
    path('proveedores/', include('apps.proveedores.urls')),  # Rutas de la app proveedores
    path('cafe/', include('apps.cafe.urls')),  # Rutas de la app cafe
    path('procesos/', include('apps.procesos.urls')),  # Rutas de la app procesos
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas de autenticación
]
