# Модуль API URLS проекта.
from django.urls import include, path
from rest_framework import routers

from .views import ContractorsViewSet

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('contractors', ContractorsViewSet, basename='contractors')

urlpatterns = [
    path("", include(router_v1.urls)),
]
