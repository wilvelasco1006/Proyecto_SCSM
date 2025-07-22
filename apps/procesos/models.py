from django.db import models
from django.utils import timezone

class ProcesoBase(models.Model):
    """Modelo base para todos los procesos productivos."""
    fecha = models.DateField(default=timezone.now)
    responsable = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    
    def delete(self, using=None, keep_parents=False):
        """Sobrescribe delete(): marca is_active=False en lugar de borrar."""
        self.is_active = False
        self.save()
        return self

class CafeTrillado(ProcesoBase):
    """Modelo para el proceso de café trillado."""
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=2, choices=[('KG', 'Kilogramos'), ('LB', 'Libras')], default='KG')
    
    def __str__(self):
        return f"Trillado: {self.fecha} - {self.cantidad} {self.unidad}"

class CafeTostado(ProcesoBase):
    """Modelo para el proceso de café tostado."""
    cantidad_baches = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Tostado: {self.fecha} - {self.cantidad_baches} baches"

class CafeMolido(ProcesoBase):
    """Modelo para el proceso de café molido."""
    cantidad_baches = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Molido: {self.fecha} - {self.cantidad_baches} baches"

class CafeEmpacado(ProcesoBase):
    """Modelo para el proceso de café empacado."""
    # Tradicional
    libras_tradicional = models.PositiveIntegerField(default=0)
    medias_tradicional = models.PositiveIntegerField(default=0)
    cuartos_tradicional = models.PositiveIntegerField(default=0)
    
    # Premium
    libras_premium = models.PositiveIntegerField(default=0)
    medias_premium = models.PositiveIntegerField(default=0)
    cuartos_premium = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        total = (self.libras_tradicional + self.medias_tradicional + self.cuartos_tradicional + 
                self.libras_premium + self.medias_premium + self.cuartos_premium)
        return f"Empacado: {self.fecha} - {total} unidades"
