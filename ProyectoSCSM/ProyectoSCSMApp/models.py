from django.db import models
import locale
# Create your models here.
# ProyectoSCSMApp/models.py


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=50, unique=True)
    #se eliminaron los atributos de email y direccion y se añadieron a Cliente
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
    #se añaden nuevos atributos
    direccion = models.TextField()
    email = models.EmailField()

    def registrar_cliente(self):
        # Aquí iría la lógica de registro del cliente, si es necesario.
        pass

class Cafe(models.Model):
    fecha_compra = models.DateField()
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=15, decimal_places=1)  # Permitir hasta 11 dígitos antes del punto y 3 después
    datos_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="cafe")

    def __str__(self):
        # Configura el formato de moneda a 'es_CO' para el símbolo de pesos
        locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')
        precio_formateado = locale.currency(self.precio, grouping=True)  # Formatea el precio con el símbolo y separadores
        return f"{self.cantidad} kg de café comprado el {self.fecha_compra} por {precio_formateado}"

    #def __str__(self):
     #   return f"{self.cantidad} kg de café comprado el {self.fecha_compra}"