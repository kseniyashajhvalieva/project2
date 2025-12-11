from unittest.mock import Mock, patch

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_number_data() -> dict:
    return {
        "valid_number": 1234567890123456,
        "short_number": 1234567890,  # 10 digits
        "only_four_digits": 3456,  # 4 digits
        "invalid_type": "abc",
    }


@pytest.fixture
def account_number_data() -> dict:
    return {
        "valid_number": 123456789012,  # 12 digits
        "short_number": 1234,  # 4 digits
        "long_number": 12345678901234567890,  # 20 digits
    }


def test_get_mask_card_number_valid(card_number_data: dict) -> None:
    """Ожидается: XXXX XX** **** XXXX"""
    assert get_mask_card_number(card_number_data["valid_number"]) == "1234 56** **** 3456"


@patch("src.masks.logger_masks")
def test_get_mask_card_number_short(mock_logger: Mock, card_number_data: dict) -> None:
    """Короткий номер карты (10 цифр) вызывает ValueError"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_number_data["short_number"])
    mock_logger.error.assert_called_once()


@patch("src.masks.logger_masks")
def test_get_mask_card_number_only_four_digits(mock_logger: Mock, card_number_data: dict) -> None:
    """Номер из 4 цифр вызывает ValueError"""
    with pytest.raises(ValueError):
        get_mask_card_number(card_number_data["only_four_digits"])
    mock_logger.error.assert_called_once()


def test_get_mask_card_number_invalid_type(card_number_data: dict) -> None:
    """Ожидается TypeError, так как функция принимает int, а передается str"""
    with pytest.raises(TypeError):
        get_mask_card_number(card_number_data["invalid_type"])


def test_get_mask_account_valid(account_number_data: dict) -> None:
    """Ожидается: **XXXX (последние 4)"""
    assert get_mask_account(account_number_data["valid_number"]) == "**9012"


def test_get_mask_account_short(account_number_data: dict) -> None:
    """Для 4 цифр: **XXXX"""
    assert get_mask_account(account_number_data["short_number"]) == "**1234"


def test_get_mask_account_long(account_number_data: dict) -> None:
    """Для длинного: **XXXX (последние 4)"""
    assert get_mask_account(account_number_data["long_number"]) == "**7890"


def test_get_mask_account_invalid_type(card_number_data: dict) -> None:
    """Ожидается TypeError, так как функция принимает int, а передается str"""
    with pytest.raises(TypeError):
        get_mask_account(card_number_data["invalid_type"])
