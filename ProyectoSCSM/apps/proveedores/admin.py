from django.contrib import admin
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'num_contacto')
    list_filter = ('nombres', 'apellidos')  # Filtro para facilitar la búsqueda por nombre y apellido
    search_fields = ('nombres', 'apellidos', 'cedula')  # Campos para búsqueda rápida

admin.site.register(Proveedor, ProveedorAdmin)