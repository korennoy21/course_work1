import json
import datetime

def get_json(file_name):
    """Читает файл json"""
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)


def sort_status(json_list, state):
    """Сортировка по статусу"""
    result = []
    for i in json_list:
        if i.get('state') == state:
            result.append(i)
    return result


def sort_dates(list_):
    """cортирует по датам"""
    return sorted(list_, key=lambda x: x['date'])


def revers(list_):
    """Разворачивает список"""
    return list_[::-1]


def format_date(value):
    """Возвращает дату"""
    date = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
    return date.strftime('%d.%m.%Y')
