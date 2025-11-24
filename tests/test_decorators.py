import pytest
from src.decorators import log


def test_log_console_success(capsys):
    """
    Проверяет, что декоратор log корректно выводит сообщение об успешном выполнении
    функции в консоль, когда filename не задан.
    """
    @log()
    def my_function(a, b):
        return a + b

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_function ok"


def test_log_console_error(capsys):
    """
    Проверяет, что декоратор log корректно выводит сообщение об ошибке
    в консоль и перевыбрасывает исключение, когда filename не задан.
    """
    @log()
    def divide_by_zero(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError) as excinfo:
        divide_by_zero(1, 0)

    captured = capsys.readouterr()
    expected_log = "divide_by_zero error: ZeroDivisionError. Inputs: (1, 0), {}"
    assert captured.out.strip() == expected_log
    assert "division by zero" in str(excinfo.value)
