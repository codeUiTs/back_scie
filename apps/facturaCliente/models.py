from django.db import models
from django.utils.timezone import now
from apps.base.models import Common

class FacturaCliente(Common):
    invoiceChoices = (
        ('Paid', 'Paid'),
        ('Draft', 'Draft'),
        ('Cancel', 'Cancel'),
        ('Process', 'Process'),
        ('Invoiced', 'Invoiced'),
    )
    class Meta:
        verbose_name = 'Factura Cliente'
        verbose_name_plural = 'Facturas Cliente'
        
    cliente = models.CharField(max_length=255, null=False)
    fecha_factura = models.DateField(null=True , default=now)
    fecha_vencimiento = models.DateField(null=True, default=now )
    total = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=255, null=True, choices=invoiceChoices, default='Draft')
    
    # def save(self, *args, **kwargs):
    #     return super(Categoria,self).save(*args, **kwargs)
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.cliente
