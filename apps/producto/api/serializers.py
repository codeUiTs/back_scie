from rest_framework import serializers
from apps.producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class ListProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude =('r_object',)
