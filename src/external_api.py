import os

import requests
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env

API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data"


def convert_currency(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли, если валюта USD или EUR.
    Возвращает сумму в рублях (float).
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency not in ["USD", "EUR"]:
        return float(amount)

    headers = {"apikey": API_KEY}
    params = {"to": "RUB", "from": currency, "amount": amount}

    try:
        response = requests.get(f"{BASE_URL}/convert", headers=headers, params=params)
        response.raise_for_status()  # Вызывает исключение для плохих статусов
        data = response.json()
        if data.get("success"):
            return float(data["result"])
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
    except (KeyError, TypeError) as e:
        print(f"Ошибка обработки данных API: {e}")

    return float(amount)  # В случае ошибки возвращаем исходную сумму
