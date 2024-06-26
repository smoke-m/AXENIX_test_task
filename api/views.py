# Модуль представлений API.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .utils import create_xls_file, check_decent_status


class ContractorsViewSet(viewsets.GenericViewSet):
    """Вьсюсет для Contractors."""

    @action(detail=False, url_path='test_action', methods=('get',))
    def create_cloudpayment(self, request):
        """Тестовый Action Contractors."""
        # create_xls_file()
        check_decent_status()
        return Response(
            dict(ok='ok'),
            status=status.HTTP_200_OK,
        )
