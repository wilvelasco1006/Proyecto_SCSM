from django.contrib import admin
from .models import Proveedor, Cafe, Cliente
import locale

class CafeAdmin(admin.ModelAdmin):
    list_display = ('fecha_compra', 'cantidad', 'precio_formateado', 'datos_proveedor')  # Campos que se muestran en columnas
    list_filter = ('fecha_compra', 'datos_proveedor')  # Filtros para la barra lateral

    def precio_formateado(self, obj):
        try:
            locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
        except locale.Error:
            # Si 'es_CO.UTF-8' no está disponible, usar configuración predeterminada
            locale.setlocale(locale.LC_ALL, '')
        
        # Comprobamos si el precio es un número entero
        if obj.precio == int(obj.precio):
            # Mostrar sin decimales y con el símbolo de pesos
            return f"${locale.format_string('%d', obj.precio, grouping=True)}"
        else:
            # Formatear con decimales y símbolo de moneda
            return locale.currency(obj.precio, grouping=True)
            
    precio_formateado.short_description = 'Precio (COP)'  # Etiqueta para la columna

# Configuración de visualización para Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'num_contacto', 'direccion', 'email')
    list_filter = ('nombres', 'apellidos')  # Filtro para facilitar la búsqueda por nombre y apellido
    search_fields = ('nombres', 'apellidos', 'cedula', 'email')  # Campos para búsqueda rápida

# Configuración de visualización para Proveedor
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'num_contacto')
    list_filter = ('nombres', 'apellidos')  # Filtro para facilitar la búsqueda por nombre y apellido
    search_fields = ('nombres', 'apellidos', 'cedula')  # Campos para búsqueda rápida


# Registro de los modelos con sus configuraciones personalizadas

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Cafe, CafeAdmin)


