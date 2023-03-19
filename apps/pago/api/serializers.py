from rest_framework import serializers
from apps.pago.models import Pago


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = "__all__"

class ListPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        exclude = ('r_object',)
