from django.db import models
from apps.base.models import Common

class LibroMayor(Common):
    class Meta:
        verbose_name = 'Libro Mayor'
        verbose_name_plural = 'Libro Mayor'
        
    diario = models.CharField(max_length=255, null=False)
    fecha_inicio = models.DateField(null=True ,auto_now_add=True)
    fecha_fin = models.DateField(null=True ,auto_now_add=True)
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.diario