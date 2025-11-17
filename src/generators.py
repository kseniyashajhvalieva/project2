from typing import Any, Dict, List, Iterator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)"""
    for transact in transactions:
        if transact.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transact
