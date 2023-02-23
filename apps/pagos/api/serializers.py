from rest_framework import serializers
from apps.pagos.models import Pagos


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        fields = "__all__"

class ListPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagos
        exclude = ('r_object',)
