from rest_framework import serializers
from apps.solicitudSuministro.models import SolicitudSuministro


class SsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSuministro
        fields = "__all__"

class ListSsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSuministro
        exclude =("r_object",)
