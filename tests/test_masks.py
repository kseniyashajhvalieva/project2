import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_number_data():
    return {
        "valid_number": 1234567890123456,
        "short_number": 1234567890,
        "long_number": 12345678901234567890,
        "only_last_four": 3456
    }

@pytest.fixture
def account_number_data():
    return {
        "valid_number": 123456789012,
        "short_number": 1234,
        "long_number": 12345678901234567890,
        "invalid_input": "abc"
    }

def test_get_mask_card_number_valid(card_number_data):
    assert get_mask_card_number(card_number_data["valid_number"]) == "1234 56** **** 3456"

def test_get_mask_card_number_short(card_number_data):
    assert get_mask_card_number(card_number_data["short_number"]) == "1234 56** **** 9012" # Учитывая, что
                                                                                           # короткий номер будет
                                                                                           # обрезаться

def test_get_mask_card_number_long(card_number_data):
    assert get_mask_card_number(card_number_data["long_number"]) == "1234 56** **** 7890" # Последние 4 цифры

def test_get_mask_card_number_only_last_four(card_number_data):
    assert get_mask_card_number(card_number_data["only_last_four"]) == "0000 00** **** 3456" # Если число < 10000,
                                                                                             # оно будет дополнено
                                                                                             # нулями

def test_get_mask_account_valid(account_number_data):
    assert get_mask_account(account_number_data["valid_number"]) == "1234"

def test_get_mask_account_short(account_number_data):
    assert get_mask_account(account_number_data["short_number"]) == "1234"

def test_get_mask_account_long(account_number_data):
    assert get_mask_account(account_number_data["long_number"]) == "7890"

def test_get_mask_account_invalid_input(account_number_data):
    with pytest.raises(ValueError): # Ожидаем ошибку, если входные данные не число
        get_mask_account(account_number_data["invalid_input"])
