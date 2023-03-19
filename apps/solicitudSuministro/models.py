from django.db import models
from apps.base.models import Common

class SolicitudSuministro(Common):
    class Meta:
        verbose_name = 'Solicitud de Suministro'
        verbose_name_plural = 'Solicitud de Suministros'
        
    producto_solicitado = models.CharField(max_length=255, null=True)    
    producto_entregado = models.CharField(max_length=255, null=True)    
    cantidad_solicitada = models.CharField(max_length=255, null=False)
    cantidad = models.CharField(max_length=255, null=False)
    cantidad_real = models.CharField(max_length=255, null=True)   
    medida = models.CharField(max_length=255, null=True)   
    partida = models.CharField(max_length=255, null=True)   
    estado = models.CharField(max_length=255, null=True)   
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.producto_solicitado