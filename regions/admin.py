# Модуль админки Регионов.
from django.conf import settings
from django.contrib import admin

from .models import Regions


@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    """Админ зона Регионов."""

    list_display = ('name', 'code')
    empty_value_display = settings.EMPTY_VALUE
