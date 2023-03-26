from rest_framework import serializers
from apps.facturaCliente.models import FacturaCliente, Cliente
from apps.producto.api.serializers import ProductoSerializer

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
        
class FcSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaCliente
        fields = "__all__"

class ListFcSerializer(serializers.ModelSerializer):
    producto = serializers.StringRelatedField(many=True)
    cliente = serializers.StringRelatedField(many=False)
    class Meta:
        model = FacturaCliente
        fields = "__all__"

class ReportFcSerializer(serializers.ModelSerializer):
    producto = serializers.StringRelatedField(many=True)
    cliente = serializers.StringRelatedField(many=False)
    class Meta:
        model = FacturaCliente
        exclude = ('r_object','uuid','descripcion')
