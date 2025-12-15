import re
from collections import Counter
from typing import List, Dict, Any


def search_by_description(data: List[Dict[str, Any]], search_str: str) -> List[Dict[str, Any]]:
    """Ищет операции по строке в описании с использованием регулярных выражений."""
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [op for op in data if op.get("description") and pattern.search(op["description"])]


def count_by_categories(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Считает операции по категориям на основе поля description."""
    descriptions = [op.get("description", "") for op in data]
    category_counts = Counter(desc for desc in descriptions if desc in categories)
    return dict(category_counts)
