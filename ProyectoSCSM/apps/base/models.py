from django.db import models

class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    num_contacto = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)  # <--- Borrado lógico

    class Meta:
        abstract = True  # Esto indica que es una clase abstracta y no se creará una tabla para ella.