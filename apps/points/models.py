from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Scale(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100
    )
    points = models.IntegerField(
        default=0, validators=(
            MinValueValidator(1),
            MaxValueValidator(10)
        )
    )

    class Meta:
        verbose_name = 'Progress scale'
        verbose_name_plural = 'Progress scales'
