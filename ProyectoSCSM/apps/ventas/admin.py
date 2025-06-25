from django.contrib import admin
from .models import Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 0
    readonly_fields = ['subtotal']

class VentaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'fecha', 'cliente', 'responsable', 'total', 'estado')
    list_filter = ('fecha', 'estado', 'cliente')
    search_fields = ('numero_factura', 'cliente__nombres', 'cliente__apellidos', 'responsable')
    readonly_fields = ('total',)
    inlines = [DetalleVentaInline]
    
    def get_readonly_fields(self, request, obj=None):
        # Hacer número de factura de solo lectura si ya existe
        if obj and obj.numero_factura:
            return self.readonly_fields + ('numero_factura',)
        return self.readonly_fields

admin.site.register(Venta, VentaAdmin)
