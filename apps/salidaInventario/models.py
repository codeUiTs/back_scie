from django.db import models
from apps.base.models import Common
from apps.producto.models import Producto

class SalidaInventario(Common):
    class Meta:
        verbose_name = 'Salida de Inventario'
        verbose_name_plural = 'Salidas de Inventario'
        
    producto_solicitado = models.ForeignKey(Producto, related_name="productoId", blank=True, null=True, on_delete=models.CASCADE)    
    cantidad_solicitada = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True) 
    importe = models.FloatField(null=True, blank=True)  
    justificacion = models.CharField(max_length=255, null=True) 
    
    def __str__(self):
        return self.uuid