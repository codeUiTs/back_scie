from django.db import models
from apps.base.models import Common

class LibroDiario(Common):
    class Meta:
        verbose_name = 'Libro Diario'
        verbose_name_plural = 'Libro Diario'
        
    diario = models.CharField(max_length=255, null=False)
    fecha_inicio = models.DateField(null=False ,auto_now_add=True)
    fecha_fin = models.DateField(null=False ,auto_now_add=True)
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.diario