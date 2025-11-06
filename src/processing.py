from typing import List, Dict, Any

def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    return [op for op in operations if op.get('state') == state]