from rest_framework import viewsets

from apps.points.models import Scale
from apps.points.serializers import ScaleSerializer


class ScaleModelViewSet(viewsets.ModelViewSet):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer

