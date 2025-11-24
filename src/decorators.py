from functools import wraps
from typing import Callable, Any


def log(filename: str ="") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
        Декоратор для логирования выполнения функций.

        Логирует начало и конец выполнения функции, ее результаты
        или возникшие ошибки в файл или консоль.

        Если имя файла для записи логов не задано, логи выводятся в консоль.
        """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_message = ""
            func_result = None

            try:
                func_result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"

            if filename:
                with open(filename, 'a') as f:
                    f.write(log_message + '\n')
            else:
                print(log_message)

            if "error" in log_message:
                raise

            return func_result
        return wrapper
    return decorator
