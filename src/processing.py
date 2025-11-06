from typing import List, Dict, Any

def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу date.
    """
    return sorted(operations, key=lambda x: x.get('date'), reverse=reverse)
