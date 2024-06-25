# Модуль модели Регионов.
from django.conf import settings
from django.db import models


class Regions(models.Model):
    """Модель Регионов."""

    name = models.CharField(max_length=settings.MAX_NAME_REGION_LENGTH)
    code = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('code',)

    def __str__(self):
        return self.code
