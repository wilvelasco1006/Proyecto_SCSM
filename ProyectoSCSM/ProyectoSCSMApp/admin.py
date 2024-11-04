from django.contrib import admin
from .models import Proveedor, Cafe, Cliente
import locale

class CafeAdmin(admin.ModelAdmin):
    list_display = ('fecha_compra', 'cantidad', 'precio_formateado', 'datos_proveedor')  # Campos que se muestran en columnas
    list_filter = ('fecha_compra', 'datos_proveedor')  # Filtros para la barra lateral

    def precio_formateado(self, obj):
        locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
        return locale.currency(obj.precio, grouping=True)  # Formatea el precio con el símbolo de moneda
    precio_formateado.short_description = 'Precio (COP)'  # Etiqueta para la columna

# Configuración de visualización para Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'num_contacto', 'direccion', 'email')
    list_filter = ('nombre',)  # Filtro para facilitar la búsqueda por nombre
    search_fields = ('nombre', 'cedula', 'email')  # Campos para búsqueda rápida

# Configuración de visualización para Proveedor
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cedula', 'num_contacto')
    list_filter = ('nombre',)  # Filtro para facilitar la búsqueda por nombre
    search_fields = ('nombre', 'cedula')  # Campos para búsqueda rápida


# Registro de los modelos con sus configuraciones personalizadas

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cafe, CafeAdmin)


