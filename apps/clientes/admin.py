from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'num_contacto', 'direccion', 'email')
    list_filter = ('nombres', 'apellidos')  # Filtro para facilitar la búsqueda por nombre y apellido
    search_fields = ('nombres', 'apellidos', 'cedula', 'email')  # Campos para búsqueda rápida

admin.site.register(Cliente, ClienteAdmin)