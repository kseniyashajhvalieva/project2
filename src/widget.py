import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета."""
    parts = data.split()
    number_str = parts[-1]

    if "Счет" in data:
        try:
            account_num = int(number_str)
            return "" + get_mask_account(account_num)
        except ValueError:
            raise ValueError("invalid literal for int() with base 10: '{}'".format(number_str))
    elif "Visa" in data or "MasterCard" in data or "Maestro" in data or "Мир" in data:
        try:
            card_num = int(number_str)
            return get_mask_card_number(card_num)
        except ValueError:
            raise ValueError("invalid literal for int() with base 10: '{}'".format(number_str))
    else:
        raise ValueError("Invalid input string for masking")


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате YYYY-MM-DDTHH:MM:SS.ffffff в строку формата "ДД.ММ.ГГГГ".

    Аргументы:
        date_string: Строка с датой в формате YYYY-MM-DDTHH:MM:SS.ffffff (например, "2024-03-11T02:26:18.671407").

    Возвращает:
        Строка с датой в формате "ДД.ММ.ГГГГ" (например, "11.03.2024").
    """
    date_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f").date()
    return date_object.strftime("%d.%m.%Y")
