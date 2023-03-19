from rest_framework import serializers
from apps.productoVendible.models import ProductoVendible


class PvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoVendible
        fields = "__all__"

class ListPvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoVendible
        exclude =('r_object',)
