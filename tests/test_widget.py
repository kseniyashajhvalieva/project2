import pytest
from src.widget import mask_account_card, get_date

@pytest.fixture
def operations_data():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "amount": 1000.0,
            "currency": "RUB",
            "description": "Перевод",
            "to": "Счет 77593040100000004561" # Для теста счета
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": 500.0,
            "currency": "RUB",
            "description": "Перевод",
            "to": "Карта Visa Classic 41428829725561076141" # Измененный формат для теста карты
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": 200.0,
            "currency": "RUB",
            "description": "Перевод",
            "to": "Счет 45678901234567890123"
        }
    ]

def test_mask_account_card_account(operations_data):
    # Тестируем маскировку счета
    account_entry = operations_data[0]
    expected_mask = "**4561" # Ожидаем ** (из masks.py) + последние 4 цифры
    assert mask_account_card(account_entry["to"]) == expected_mask

def test_mask_account_card_card(operations_data):
    # Тестируем маскировку карты
    card_entry = operations_data[1]
    expected_mask = "4142 88** **** 6141" # Ожидаем ** (из masks.py)
    assert mask_account_card(card_entry["to"]) == expected_mask

def test_mask_account_card_invalid_input():
    # Тестируем некорректный ввод
    with pytest.raises(ValueError, match="Invalid input string for masking"):
        mask_account_card("Invalid input")
    with pytest.raises(ValueError, match="invalid literal for int() with base 10: 'abc'"):
        mask_account_card("Счет abc")
    with pytest.raises(ValueError, match="invalid literal for int() with base 10: 'abc'"):
        mask_account_card("Карта abc")

def test_get_date_valid_format():
    # Тестируем корректный формат даты
    date_string = "2024-03-11T02:26:18.671407"
    expected_date = "11.03.2024"
    assert get_date(date_string) == expected_date

def test_get_date_different_format():
    # Тестируем другую строку с датой
    date_string = "2023-12-25T10:00:00.000000"
    expected_date = "25.12.2023"
    assert get_date(date_string) == expected_date

def test_get_date_invalid_format():
    # Тестируем некорректный формат даты
    with pytest.raises(ValueError):
        get_date("2024/03/11")
    with pytest.raises(ValueError):
        get_date("March 11, 2024")
    with pytest.raises(ValueError):
        get_date("2024-03-11") # Нет времени
