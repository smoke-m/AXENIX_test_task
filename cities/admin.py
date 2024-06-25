# Модуль админки Городов.
from django.conf import settings
from django.contrib import admin

from .models import Sities


@admin.register(Sities)
class SitiesAdmin(admin.ModelAdmin):
    """Админ зона Городов."""

    list_display = ('name', 'region')
    list_filter = ('region',)
    empty_value_display = settings.EMPTY_VALUE
