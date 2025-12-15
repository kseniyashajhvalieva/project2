from typing import Any, Dict
from unittest.mock import Mock, patch

import pandas as pd

from src.transactions import csv_transactions, excel_transactions


@patch("pandas.read_csv")
def test_csv_transactions(mock_read_csv: Mock) -> None:
    """Проверяет корректное чтение CSV файла и преобразование в список словарей."""
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100, 200], "currency": ["USD", "EUR"]})
    mock_read_csv.return_value = mock_data

    result: list[Dict[str, Any]] = csv_transactions("dummy.csv")

    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["currency"] == "EUR"
    mock_read_csv.assert_called_once_with("dummy.csv")


def test_csv_empty_file() -> None:
    """Проверяет, что функция возвращает пустой список при отсутствии данных."""
    with patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame()
        result: list[Dict[str, Any]] = csv_transactions("empty.csv")
        assert result == []


@patch("pandas.read_excel")
def test_excel_transactions(mock_read_excel: Mock) -> None:
    """Проверяет корректное чтение Excel файла и преобразование в список словарей."""
    mock_data = pd.DataFrame({"id": [3, 4], "amount": [300, 400], "state": ["EXECUTED", "CANCELED"]})
    mock_read_excel.return_value = mock_data

    result: list[Dict[str, Any]] = excel_transactions("dummy.xlsx")

    assert len(result) == 2
    assert result[0]["state"] == "EXECUTED"
    assert result[1]["amount"] == 400
    mock_read_excel.assert_called_once_with("dummy.xlsx")
