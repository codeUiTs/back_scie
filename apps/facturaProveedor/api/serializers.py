from rest_framework import serializers
from apps.facturaProveedor.models import FacturaProveedor
from apps.proveedor.models import Proveedor
from apps.producto.api.serializers import ProductoSerializer

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"
        
class FpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaProveedor
        fields = "__all__"

class ListFpSerializer(serializers.ModelSerializer):
    producto = serializers.StringRelatedField(many=True)
    proveedor = serializers.StringRelatedField(many=False)
    class Meta:
        model = FacturaProveedor
        fields = "__all__"

class ReportFpSerializer(serializers.ModelSerializer):
    producto = serializers.StringRelatedField(many=True)
    proveedor = serializers.StringRelatedField(many=False)
    class Meta:
        model = FacturaProveedor
        exclude = ('r_object','uuid','descripcion')
