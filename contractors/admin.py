# Модуль админки Контрагентов.
from django.conf import settings
from django.contrib import admin

from .models import Contractors


@admin.register(Contractors)
class ContractorsAdmin(admin.ModelAdmin):
    """Админ зона Контрагентов."""

    list_display = ('name', 'inn', 'kpp', 'region', 'city', 'decent')
    list_filter = ('decent',)
    empty_value_display = settings.EMPTY_VALUE
