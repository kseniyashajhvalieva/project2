from typing import Generator
from unittest.mock import patch

import pytest
import requests

from src.external_api import convert_currency


@pytest.fixture(autouse=True)
def mock_env_vars() -> Generator[None, None, None]:
    """Мокирует os.getenv для EXCHANGE_RATE_API_KEY."""
    with patch("os.getenv", return_value="dummy_api_key"):
        yield


@pytest.mark.parametrize(
    "transaction, mock_api_response, api_call_expected, expected_amount",
    [
        # Успешная конвертация USD в RUB
        ({"amount": 100, "currency": "USD"}, {"success": True, "result": 9000.0}, True, 9000.0),
        # Рублевая транзакция, без конвертации
        ({"amount": 500, "currency": "RUB"}, None, False, 500.0),
        # API вернул ошибку, возвращаем исходную сумму
        ({"amount": 50, "currency": "EUR"}, {"success": False, "error": "some_error"}, True, 50.0),
        # Запрос к API вызвал исключение, возвращаем исходную сумму
        ({"amount": 75, "currency": "USD"}, requests.exceptions.RequestException, True, 75.0),
    ],
)
def test_convert_currency_parametrized_short(
    transaction: dict,
    mock_api_response: dict | type[Exception] | None,
    api_call_expected: bool,
    expected_amount: float,
) -> None:
    """Проверяет основные сценарии конвертации и ошибок."""
    with patch("requests.get") as mock_get:
        if api_call_expected:
            mock_get.return_value.status_code = 200  # Для всех API-вызовов
            mock_get.return_value.raise_for_status.return_value = None  # По умолчанию нет HTTP ошибки

            if isinstance(mock_api_response, dict):
                mock_get.return_value.json.return_value = mock_api_response
            elif isinstance(mock_api_response, type) and issubclass(mock_api_response, Exception):
                mock_get.return_value.raise_for_status.side_effect = mock_api_response

        result = convert_currency(transaction)

        assert result == expected_amount
        if api_call_expected:
            mock_get.assert_called_once()
        else:
            mock_get.assert_not_called()
