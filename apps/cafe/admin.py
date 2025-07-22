from django.contrib import admin
from .models import Cafe
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

admin.site.register(Cafe, CafeAdmin)