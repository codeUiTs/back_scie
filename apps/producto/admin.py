from django.contrib import admin
from apps.producto.models import Producto, Categoria, UOM

admin.site.register(Categoria)
admin.site.register(UOM)
admin.site.register(Producto)