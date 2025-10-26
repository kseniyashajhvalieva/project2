import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета."""
    if "Счет" in data:
        return get_mask_account(int(data.split()[-1]))
    else:
        return get_mask_card_number(int(data.split()[-1]))


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате ДД.ММ.ГГГГ в строку формата "ДД месяц ГГГГ".

    Args:
        date_string: Строка с датой в формате ДД.ММ.ГГГГ (например, "26.10.2023").

    Returns:
        Строка с датой в формате "ДД месяц ГГГГ" (например, "26 октября 2023").
    """
    date_object = datetime.datetime.strptime(date_string, "%d.%m.%Y").date()
    month_name = date_object.strftime("%B")
    month_name_ru = {
        "January": "января",
        "February": "февраля",
        "March": "марта",
        "April": "апреля",
        "May": "мая",
        "June": "июня",
        "July": "июля",
        "August": "августа",
        "September": "сентября",
        "October": "октября",
        "November": "ноября",
        "December": "декабря",
    }[month_name]
    return f"{date_object.day} {month_name_ru} {date_object.year}"
