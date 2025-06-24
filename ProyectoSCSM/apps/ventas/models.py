from django.db import models
from apps.clientes.models import Cliente
import uuid

class Venta(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    numero_factura = models.CharField(max_length=10, unique=True, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    fecha = models.DateField()
    responsable = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    is_active = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha', '-fecha_creacion']
    
    def save(self, *args, **kwargs):
        # Generar número de factura automáticamente si no existe
        if not self.numero_factura:
            # Obtener último número de factura
            ultimo_num = Venta.objects.order_by('-numero_factura').first()
            if ultimo_num and ultimo_num.numero_factura:
                try:
                    num = int(ultimo_num.numero_factura) + 1
                    self.numero_factura = f"{num:08d}"
                except ValueError:
                    self.numero_factura = "00000001"
            else:
                self.numero_factura = "00000001"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Venta {self.numero_factura} - {self.cliente.nombres} {self.cliente.apellidos}"
    
    def actualizar_total(self):
        """Actualiza el total de la venta basado en los detalles"""
        self.total = sum(detalle.subtotal for detalle in self.detalles.all())
        self.save()

class DetalleVenta(models.Model):
    TIPO_CAFE_CHOICES = (
        ('tradicional', 'Café Tradicional'),
        ('premium', 'Café Premium'),
    )
    
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    tipo_cafe = models.CharField(max_length=20, choices=TIPO_CAFE_CHOICES)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    def save(self, *args, **kwargs):
        # Calcular subtotal automáticamente
        self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)
        # Actualizar el total de la venta
        self.venta.actualizar_total()
    
    def __str__(self):
        return f"{self.cantidad} unidad(es) de {self.get_tipo_cafe_display()}"