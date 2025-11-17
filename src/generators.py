from itertools import count
from typing import Any, Dict, List, Iterator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    for transact in transactions:
        if transact.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transact


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transact in transactions:
        result_description = transact.get("description")
        if result_description != None:
            yield result_description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Принимает начальное и конечное значения для генерации диапазона номеров"""
    for st in range(start, stop+1):
        st_str = str(st)
        while len(st_str) < 16:
            st_str = "0" + st_str
        card_number_gen = f"{st_str[:4]} {st_str[4:8]} {st_str[8:12]} {st_str[12:]}"
        yield card_number_gen
