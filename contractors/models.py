# Модуль модели Контрагентов.
from django.conf import settings
from django.db import models

from regions.models import Regions
from cities.models import Cities


class Contractors(models.Model):
    """Модель Контрагентов."""

    name = models.CharField(max_length=settings.MAX_NAME_CONTRACTORS_LENGTH)
    inn = models.PositiveIntegerField()
    kpp = models.PositiveIntegerField()
    region = models.ForeignKey(
        Regions,
        on_delete=models.CASCADE,
        related_name='contractor',
    )
    city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        related_name='contractor',
    )
    decent = models.BooleanField()
