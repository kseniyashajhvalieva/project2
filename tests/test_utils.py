from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_json_file


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_read_json_file_success(mock_open_file: MagicMock, mock_exists: MagicMock) -> None:
    """Тест: успешное чтение валидного JSON-файла."""
    mock_exists.return_value = True
    result = read_json_file("dummy_path.json")
    assert result == [{"id": 1, "amount": 100}]


def test_read_json_file_not_found_or_invalid() -> None:
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
