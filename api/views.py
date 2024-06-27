# Модуль представлений API.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from decent_test.send_mesage import sender


class ContractorsViewSet(viewsets.GenericViewSet):
    """Вьсюсет для Contractors."""

    @action(detail=False, url_path='get_xls', methods=('post',))
    def create_cloudpayment(self, request):
        """Тестовый Action Contractors."""
        try:
            sender(request.data.get('email'))
            return Response(
                dict(ok='ok'),
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                dict(error=str(error)),
                status=status.HTTP_400_BAD_REQUEST,
            )
