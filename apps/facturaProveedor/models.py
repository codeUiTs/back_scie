from django.db import models
from apps.base.models import Common
from apps.producto.models import Producto
from apps.proveedor.models import Proveedor
from django.utils.timezone import now
class FacturaProveedor(Common):
    class Meta:
        verbose_name = 'Factura de proveedor'
        verbose_name_plural = 'Factura de proveedor'
        
    proveedor = models.ForeignKey(Proveedor,null=True, related_name="proveedorId", on_delete=models.CASCADE)
    fecha_factura = models.DateField(null=True , default=now)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    producto = models.ManyToManyField(Producto, blank=True)
    importe = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.fecha_factura