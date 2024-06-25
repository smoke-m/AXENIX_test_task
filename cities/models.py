# Модуль модели Городов.
from django.conf import settings
from django.db import models


class Sities(models.Model):
    """Модель Городов."""

    name = models.CharField(max_length=settings.MAX_NAME_SITIES_LENGTH)
    region = models.CharField(max_length=settings.MAX_REGION_SITIES_LENGTH)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
