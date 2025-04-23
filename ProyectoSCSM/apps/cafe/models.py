from django.db import models
from apps.proveedores.models import Proveedor  # Importa el modelo Proveedor

class Cafe(models.Model):
    fecha_compra = models.DateField()
    cantidad = models.FloatField()
    precio = models.IntegerField()
    datos_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="cafe")
    is_active = models.BooleanField(default=True)  # Campo para el borrado lógico

    # Manager que sólo devuelve activos
    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_active=True)

    objects = ActiveManager()  # Por defecto, sólo devuelve activos
    all_objects = models.Manager()  # Para obtener todos los objetos, incluidos los inactivos

    def delete(self, using=None, keep_parents=False):
        """Sobrescribe delete(): marca is_active=False en lugar de borrar."""
        self.is_active = False
        self.save()
    def __str__(self):
        return f"{self.cantidad} kg de café comprado el {self.fecha_compra} por {self.precio}"