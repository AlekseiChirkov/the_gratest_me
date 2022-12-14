from django.db.utils import IntegrityError

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from apps.points.models import Scale
from apps.points.serializers import ScaleSerializer


class ScaleModelViewSet(viewsets.ModelViewSet):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer

    def get_queryset(self) -> Scale:
        """
        Return QuerySet with objects related to user.
        :return: Scale QuerySet
        """

        return self.queryset.filter(user_id=self.request.user.id)

    def perform_create(self, serializer: ScaleSerializer) -> None:
        """
        Create object with current user by default.
        :param serializer: ScaleSerializer
        :return: None
        """

        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError(
                {"detail": "Scale with provided name already exist"}
            )
