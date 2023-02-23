from rest_framework import serializers
from apps.libroDiario.models import LibroDiario


class LdSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDiario
        fields = "__all__"

class ListLdSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroDiario
        exclude = ('r_object',)
