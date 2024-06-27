# Модуль утилит проекта.
import http
import json
import os
import xlwt

from celery import shared_task
from django.conf import settings
import requests
from requests.exceptions import HTTPError, RequestException

from contractors.models import Contractors


def create_xls_file():
    """"Создание xls файла из БД."""

    arr = []
    query = Contractors.objects.exclude(decent='Ok')
    for obj in query:
        arr.append(
            [obj.region.code, obj.city.name, obj.name, obj.inn, obj.decent]
        )

    directory = 'files'
    if not os.path.exists(directory):
        os.makedirs(directory)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet')
    columns = [
        'Код региона', 'Наименование населенного пункта', 'ФИО контрагента',
        'ИНН', 'Дата блокировки',
    ]

    for col_num, header in enumerate(columns):
        sheet.write(0, col_num, header)

    for row_num, row_data in enumerate(arr, start=1):
        for col_num, cell_data in enumerate(row_data):
            sheet.write(row_num, col_num, cell_data)

    file_path = os.path.join(directory, 'data.xls')
    workbook.save(file_path)


def get_api_answer(inn):
    """
    Функция выполняет запрос к API ofdata,
    выбирает нужные данные из запроса.
    """
    try:
        api_answer = requests.get(settings.URL_OFDATA.format(str(inn)))
        if api_answer.status_code != http.HTTPStatus.OK:
            raise HTTPError(f'API ofdata вернул: {api_answer.status_code}')
        answer = api_answer.json()
        return answer.get('data')
    except json.JSONDecodeError as error:
        raise json.JSONDecodeError(f'Ошибка декодирования JSON: {error}')
    except RequestException as error:
        raise RuntimeError(f'API сервиса ofdata недоступен: {error}')


def check_decent_status():
    """Проверка статуса поставщика и запись в БД."""

    query = Contractors.objects.all()
    arr_inn = [obj.inn for obj in query]
    for inn in arr_inn:
        obj = Contractors.objects.get(inn=inn)
        answer = get_api_answer(inn)
        if obj.decent == 'Ok' and answer['НедобПост'] is True:
            obj.decent = answer['НедобПостЗап'][0]['ДатаУтв']
            obj.save(update_fields=['decent'])
        elif obj.decent != 'Ok' and answer['НедобПост'] is False:
            obj.decent = 'Ok'
            obj.save(update_fields=['decent'])


@shared_task
def test_cel():
    """Задача селери по таймингу."""
    try:
        check_decent_status()
        create_xls_file()
    except Exception as error:
        print(error)
