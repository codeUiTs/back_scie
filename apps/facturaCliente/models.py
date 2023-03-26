from django.db import models
from django.utils.timezone import now
from apps.base.models import Common
from apps.producto.models import Producto

class Cliente(Common):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    nombre = models.CharField(max_length=255, null=False)
    email= models.EmailField(null=True , blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        """Unicode representation of Material."""
        return self.nombre
class FacturaCliente(Common):
    class Meta:
        verbose_name = 'Factura Cliente'
        verbose_name_plural = 'Facturas Cliente'
        
    cliente = models.ForeignKey(Cliente, related_name="clienteId", on_delete=models.CASCADE)
    fecha_factura = models.DateField(null=True , default=now)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    producto = models.ManyToManyField(Producto, blank=True)
    importe = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        """Unicode representation of Material."""
        return f"{self.fecha_factura}"
