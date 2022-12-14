from rest_framework import serializers

from apps.points.models import Scale


class ScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scale
        fields = '__all__'
