from rest_framework import serializers
from apps.facturaCliente.models import FacturaCliente


class FcSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaCliente
        fields = "__all__"

class ListFcSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaCliente
        fields = ('id','cliente', 'fecha_factura', 'fecha_vencimiento', 'total', 'estado')
