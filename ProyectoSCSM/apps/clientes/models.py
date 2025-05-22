from django.db import models
from apps.base.models import Persona

class Cliente(Persona):
    direccion = models.TextField()
    email = models.EmailField()

    def registrar_cliente(self):
        pass
    # Manager que sólo devuelve activos
    class ActiveManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_active=True)

    objects     = ActiveManager()    # por defecto sólo activos
    all_objects = models.Manager()   # para todos (incluyendo borrados)

    def delete(self, using=None, keep_parents=False):
        """Sobrescribe delete(): marca is_active=False en lugar de borrar."""
        self.is_active = False
        self.save()
        return self