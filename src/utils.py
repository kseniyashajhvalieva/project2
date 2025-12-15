import json
import logging
import os
from typing import Any, Dict

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w")
logger.addHandler(file_handler)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)


def read_json_file(file_path: str) -> list[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список операций."""
    logger.debug(f"Попытка чтения JSON файла: {file_path}")
    try:
        if not os.path.exists(file_path):
            logger.error(f"Файл не найден по пути: {file_path}")
            return []
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно прочитан JSON файл: {file_path}. Данные являются списком.")
                return data
            else:
                logger.warning(
                    f"JSON файл {file_path} прочитан, но корневой элемент не является списком. "
                    f"Возвращается пустой список."
                )
                return []
    except FileNotFoundError:
        logger.error(f"Файл не найден по пути: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}", exc_info=True)
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка при чтении файла {file_path}: {e}", exc_info=True)
        return []


def transaction_description(transaction: Dict[str, Any]) -> str:
    logger.debug(f"Получение описания для транзакции ID: {transaction.get('id', 'N/A')}")
    description = str(transaction.get("description", "Описание отсутствует"))
    logger.info(f"Описание транзакции ID {transaction.get('id', 'N/A')}: '{description}'")
    return description


def get_transaction_amount(transaction: Dict[str, Any]) -> str:
    logger.debug(f"Получение суммы для транзакции ID: {transaction.get('id', 'N/A')}")
    try:
        amount = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["name"]
        full_amount = f"{amount} {currency}"
        logger.info(f"Сумма транзакции ID {transaction.get('id', 'N/A')}: {full_amount}")
        return full_amount
    except (KeyError, TypeError) as e:
        logger.error(
            f"Отсутствует ключ или ошибка типа при получении суммы транзакции ID "
            f"{transaction.get('id', 'N/A')}: {e}",
            exc_info=True,
        )
        return "Сумма недоступна"
    except Exception as e:
        logger.error(
            f"Неизвестная ошибка при получении суммы транзакции ID " f"{transaction.get('id', 'N/A')}: {e}",
            exc_info=True,
        )
        return "Сумма недоступна"
