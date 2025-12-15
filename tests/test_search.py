import pytest
from src.search import search_by_description, count_by_categories


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


def test_search_by_description_not_found():
    """Тест поиска операций по строке в описании - ничего не найдено."""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"}
    ]
    result = search_by_description(data, "покупка")
    assert len(result) == 0


def test_count_by_categories():
    """Тест подсчета операций по категориям."""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод организации"},
        {"id": 4, "description": "Перевод со счета на счет"}
    ]
    categories = ["Перевод организации", "Открытие вклада"]
    result = count_by_categories(data, categories)
    assert result == {"Перевод организации": 2, "Открытие вклада": 1}


def test_count_by_categories_empty():
    """Тест подсчета операций по категориям - нет совпадений."""
    data = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Перевод со счета на счет"}
    ]
    categories = ["Пополнение счета", "Снятие наличных"]
    result = count_by_categories(data, categories)
    assert result == {}
