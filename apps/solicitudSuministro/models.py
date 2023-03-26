from django.db import models
from apps.base.models import Common
from apps.producto.models import Producto
class SolicitudSuministro(Common):
    class Meta:
        verbose_name = 'Solicitud de Suministro'
        verbose_name_plural = 'Solicitud de Suministros'
        
    producto_solicitado = models.ForeignKey(Producto, related_name="productoSolicitado", blank=True, null=True, on_delete=models.CASCADE)    
    producto_entregado = models.ForeignKey(Producto, related_name="productoEntregado", blank=True, null=True, on_delete=models.CASCADE)   
    cantidad_solicitada = models.CharField(max_length=255, null=True, blank=True)
    cantidad = models.CharField(max_length=255, null=True, blank=True)  
    estado = models.CharField(max_length=255, null=True)   
    
    def __str__(self):
        """Unicode representation of Material."""
        return f"{self.producto_solicitado}"