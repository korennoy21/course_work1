import json
def get_json(file_name) -> list:
    """Читает файл json"""
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)
