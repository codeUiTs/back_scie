from django.db import models
from apps.base.models import Common

class Pago(Common):
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        
    tipo = models.CharField(max_length=255, null=True, choices=(('Cliente', 'Cliente'), ('Proveedor', 'Proveedor')))    
    destino = models.CharField(max_length=255, null=True)  
    fecha_pago = models.DateField(null=True ,auto_now_add=True)
    cantidad = models.FloatField(null=True, blank=True)  
    concepto = models.CharField(max_length=255, null=True)  
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.concepto