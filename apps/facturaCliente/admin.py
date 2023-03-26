from django.contrib import admin
from apps.facturaCliente.models import FacturaCliente, Cliente

admin.site.register(Cliente)
admin.site.register(FacturaCliente)
