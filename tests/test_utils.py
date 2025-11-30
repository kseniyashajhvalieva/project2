import json
from unittest.mock import mock_open, patch
from src.utils import read_json_file

def test_read_json_file_success():
    """Тест: успешное чтение валидного JSON-файла."""
    mock_data = json.dumps([{"id": 1, "amount": 100}])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("dummy_path.json")
        assert result == [{"id": 1, "amount": 100}]

def test_read_json_file_not_found_or_invalid():
    """Тест: файл не найден, пуст или JSON невалиден/не список."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("non_existent_path.json")
        assert result == []
    with patch("builtins.open", mock_open(read_data="")):
        result = read_json_file("empty_file.json")
        assert result == []
    with patch("builtins.open", mock_open(read_data="not a json")):
        result = read_json_file("invalid_json.json")
        assert result == []
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        result = read_json_file("not_list.json")
        assert result == []
