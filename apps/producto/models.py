from django.db import models
from apps.base.models import Common
    
class Categoria(Common):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    nombre = models.CharField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return self.nombre
    
class UOM(Common):
    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
        
    nombre = models.CharField(max_length=255, null=True, unique=True)
    
    def __str__(self):
        return self.nombre
class Producto(Common):
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    nombre = models.CharField(max_length=255, null=True, unique=True)    
    precio_unitario = models.CharField(max_length=255, null=False)
    unidades_disponibles = models.IntegerField(null=True, blank=True) 
    vendible = models.BooleanField(default=False)  
    comprable = models.BooleanField(default=False)
    activo = models.BooleanField(default=False) 
    categoria = models.ForeignKey(Categoria, related_name="subcategoria", blank=True, null=True, on_delete=models.CASCADE) 
    uom = models.ForeignKey(UOM, related_name="subuom", blank=True, null=True, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.nombre
