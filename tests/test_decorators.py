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
