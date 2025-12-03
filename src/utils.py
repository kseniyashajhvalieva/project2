import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/utils.log', mode='w')
logger.addHandler(file_handler)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)


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
