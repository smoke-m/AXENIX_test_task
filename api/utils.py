# Модуль утилит проекта.
import os
import xlwt

from contractors.models import Contractors


def create_xls_file():
    """"Создание xls файла из БД."""

    arr = []
    query = Contractors.objects.filter(decent=False)
    for obj in query:
        arr.append([obj.region.code, obj.city.name, obj.name, obj.inn])

    directory = 'files'
    if not os.path.exists(directory):
        os.makedirs(directory)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet')
    columns = [
        'Код региона', 'Наименование населенного пункта', 'ФИО контрагента',
        'ИНН',
    ]

    for col_num, header in enumerate(columns):
        sheet.write(0, col_num, header)

    for row_num, row_data in enumerate(arr, start=1):
        for col_num, cell_data in enumerate(row_data):
            sheet.write(row_num, col_num, cell_data)

    file_path = os.path.join(directory, 'data.xls')
    workbook.save(file_path)


def check_decent_status():
    """Проверка статуса поставщика."""

    query = Contractors.objects.all()
    arr_inn = [obj.inn for obj in query]
    print(arr_inn)
