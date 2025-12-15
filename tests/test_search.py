import pytest
from src.search import search_by_description


def test_search_by_description_found():
    """Тест поиска операций по строке в описании - успешный поиск."""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод со счета на счет"}
    ]
    result = search_by_description(data, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3
