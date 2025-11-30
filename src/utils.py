import json


def read_json_file(file_path: str) -> list:
    """Читает JSON-файл и возвращает список операций."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return []
