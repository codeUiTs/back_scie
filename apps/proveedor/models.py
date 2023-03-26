from django.db import models
from apps.base.models import Common

class Proveedor(Common):
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        
    nombre = models.CharField(max_length=255, null=False, blank=True)
    direccion = models.CharField(max_length=255, null=False, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    
    
    def __str__(self):
        return self.nombre