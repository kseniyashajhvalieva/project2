from typing import Any, Dict, List


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей операций по заданному статусу.

    Аргументы:
        operations (list[dict[str, Any]]): Список словарей с банковскими операциями.
        state (str, optional): Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

    Возвращает:
        list[dict[str, Any]]: Новый список словарей, содержащий только отфильтрованные операции.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей операций по дате.

    Аргументы:
        operations (list[dict[str, Any]]): Список словарей с банковскими операциями.
        reverse (bool, optional): Порядок сортировки.
                                  True для убывающего (от новых к старым),
                                  False для возрастающего. По умолчанию True.

    Возвращает:
        list[dict[str, Any]]: Новый список словарей, отсортированный по дате.
    """
    return sorted(operations, key=lambda x: x.get("date", "1970-01-01T00:00:00.000000"), reverse=reverse)
