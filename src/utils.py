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


def get_from_to(dict_, from_, to_):
    """Вернет откуда карта/счет, куда карта/счет"""
    from_transaction = dict_.get(from_)
    to_transaction = dict_.get(to_)
    if from_transaction is None:
        return False, to_transaction
    return from_transaction, to_transaction


def cipher(str_):
    """на вход получает  <<Счет 65298957349197687907>>
       или <<Visa Classic 3414396880443483>>
       возвращает  номер счета в шифровaнном виде"""
    if not str_:
        return None
    elif "счет" in str_.lower():
        _name = str_.split()[:-1]
        _number = str_.split()[-1]
        result = f"{' '.join(_name)} **{_number[-4:]}"
        return result
    else:
        card_name = str_.split()[:-1]
        card_number = str_.split()[-1]
        result = f"{' '.join(card_name)} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        return result
