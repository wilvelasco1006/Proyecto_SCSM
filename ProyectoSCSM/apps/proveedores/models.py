from django.db import models
from apps.base.models import Persona

class Proveedor(Persona):
    def registrar_proveedor(self):
        pass
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
        """Devuelve una representación legible del proveedor."""
        return f"{self.nombres} "