from django.db import models

# Create your models here.
# ProyectoSCSMApp/models.py


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    direccion = models.TextField()
    num_contacto = models.CharField(max_length=20)

    class Meta:
        abstract = True  # Define que es una clase abstracta

    def __str__(self):
        return self.nombre

class Proveedor(Persona):
    # No es necesario añadir más campos, ya que hereda de Persona
    def registrar_proveedor(self):
        # Aquí iría la lógica de registro del proveedor, si es necesario.
        pass

class Cliente(Persona):
    def registrar_cliente(self):
        # Aquí iría la lógica de registro del cliente, si es necesario.
        pass

class Cafe(models.Model):
    fecha_compra = models.DateField()
    cantidad = models.FloatField()
    precio = models.FloatField()
    datos_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="cafe")

    def __str__(self):
        return f"{self.cantidad} kg de café comprado el {self.fecha_compra}"