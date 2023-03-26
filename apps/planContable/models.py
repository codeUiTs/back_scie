from django.db import models
from apps.base.models import Common
from apps.facturaCliente.models import Cliente
class Cuenta(Common):
    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
    nombre = models.CharField(max_length=255, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, related_name="cuentaClienteId", on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255, null=True, blank=True, choices=(('Deudora', 'Deudora'), ('Acreedora', 'Acreedora')))
    def __str__(self):
        return self.nombre
class PlanContable(Common):
    class Meta:
        verbose_name = 'Plan contable'
        verbose_name_plural = 'Plan contable'
    codigo = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=False)
    tipo = models.CharField(max_length=255, null=True, blank=True, choices=(('Ingreso', 'Ingreso'), ('Depreciacion', 'Depreciacion'), ('Gastos', 'Gastos'), ('Otros', 'Otros')))
    cuenta = models.ForeignKey(Cuenta, null=True, blank=True, related_name="cuentaId", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigo