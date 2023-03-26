from rest_framework import serializers
from apps.solicitudSuministro.models import SolicitudSuministro


class SsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSuministro
        fields = "__all__"

class ListSsSerializer(serializers.ModelSerializer):
    producto_solicitado = serializers.StringRelatedField(many=False)
    producto_entregado = serializers.StringRelatedField(many=False)
    class Meta:
        model = SolicitudSuministro
        fields = "__all__"