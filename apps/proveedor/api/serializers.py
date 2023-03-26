from rest_framework import serializers
from apps.proveedor.models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"

class ListProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"
