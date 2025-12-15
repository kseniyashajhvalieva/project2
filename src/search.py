import re

from typing import List, Dict, Any


def search_by_description(data: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """Ищет операции по строке в описании с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [op for op in data if op.get("description") and pattern.search(op["description"])]
