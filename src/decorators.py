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
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            log_message: str = ""
            func_result: Any = None
            caught_exception: Any = None

            try:
                func_result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"  # Используй __name__
                caught_exception = e

            if filename:
                with open(filename, 'a') as f:
                    f.write(log_message + '\n')
            else:
                print(log_message)

            if caught_exception:
                raise caught_exception

            return func_result
        return wrapper
    return decorator
