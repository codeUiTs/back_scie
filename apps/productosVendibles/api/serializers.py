from rest_framework import serializers
from apps.productosVendibles.models import ProductosVendibles


class PvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosVendibles
        fields = "__all__"

class ListPvSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductosVendibles
        exclude =('r_object',)
