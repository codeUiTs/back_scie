from rest_framework import serializers
from apps.solicitudSuministros.models import SolicitudSuministros


class SsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSuministros
        fields = "__all__"

class ListSsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudSuministros
        exclude =("r_object",)
