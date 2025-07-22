from django.contrib import admin
from .models import CafeTrillado, CafeTostado, CafeMolido, CafeEmpacado

@admin.register(CafeTrillado)
class CafeTrilladorAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'cantidad', 'unidad', 'responsable', 'is_active')
    list_filter = ('fecha', 'unidad', 'is_active')
    search_fields = ('responsable', 'fecha')

@admin.register(CafeTostado)
class CafeTostadoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'cantidad_baches', 'responsable', 'is_active')
    list_filter = ('fecha', 'is_active')
    search_fields = ('responsable', 'fecha')

@admin.register(CafeMolido)
class CafeMolidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'cantidad_baches', 'responsable', 'is_active')
    list_filter = ('fecha', 'is_active')
    search_fields = ('responsable', 'fecha')

@admin.register(CafeEmpacado)
class CafeEmpacadoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'get_total_empaques', 'responsable', 'is_active')
    list_filter = ('fecha', 'is_active')
    search_fields = ('responsable', 'fecha')
    
    def get_total_empaques(self, obj):
        total = (obj.libras_tradicional + obj.medias_tradicional + obj.cuartos_tradicional + 
                obj.libras_premium + obj.medias_premium + obj.cuartos_premium)
        return total
    get_total_empaques.short_description = 'Total de empaques'