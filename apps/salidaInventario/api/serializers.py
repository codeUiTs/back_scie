from rest_framework import serializers
from apps.salidaInventario.models import SalidaInventario


class SalidaInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalidaInventario
        fields = "__all__"

class ListSalidaInventarioSerializer(serializers.ModelSerializer):
    producto_solicitado = serializers.StringRelatedField(many=False)

    class Meta:
        model = SalidaInventario
        fields = "__all__"