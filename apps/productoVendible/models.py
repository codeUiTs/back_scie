from django.db import models
from apps.base.models import Common

class ProductoVendible(Common):
    class Meta:
        verbose_name = 'Producto Vendible'
        verbose_name_plural = 'Productos Vendibles'
        
    nombre = models.CharField(max_length=255, null=True, unique=True)    
    precio_unitario = models.CharField(max_length=255, null=False)
    unidades_disponibles = models.CharField(max_length=255, null=True)   
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.nombre