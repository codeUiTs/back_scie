from rest_framework import serializers
from apps.planContable.models import PlanContable, Cuenta


class PlanContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanContable
        fields = "__all__"

class ListPlanContableSerializer(serializers.ModelSerializer):
    cuenta = serializers.StringRelatedField(many=False)
    class Meta:
        model = PlanContable
        fields = "__all__"
        
class ListCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"
