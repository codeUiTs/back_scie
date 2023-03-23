from django.db import models
from apps.base.models import Common

class ReporteFinanciero(Common):
    class Meta:
        verbose_name = 'Reporte Financiero'
        verbose_name_plural = 'Reportes Financieros'
        
    diario = models.CharField(max_length=255, null=False)
    fecha_inicio = models.DateField(null=False ,auto_now_add=True)
    fecha_fin = models.DateField(null=False ,auto_now_add=True)
    
    def __str__(self):
        return self.diario