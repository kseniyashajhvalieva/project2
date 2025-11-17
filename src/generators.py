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
