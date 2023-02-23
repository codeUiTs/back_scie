from rest_framework import serializers
from apps.libroMayor.models import LibroMayor


class LmSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroMayor
        fields = "__all__"

class ListLmSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibroMayor
        exclude = ('r_object',)
