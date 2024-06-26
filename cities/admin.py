# Модуль админки Городов.
from django.conf import settings
from django.contrib import admin

from .models import Cities


@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    """Админ зона Городов."""

    list_display = ('name', 'region')
    list_filter = ('region',)
    empty_value_display = settings.EMPTY_VALUE
