import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger_masks = logging.getLogger(__name__)
file_handler_masks = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
logger_masks.addHandler(file_handler_masks)
formatter_masks = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_masks.setFormatter(formatter_masks)
logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты, показывая только первые 6 и последние 4 цифры.

    Аргументы:
        card_number: Номер карты в виде числа.

    Возвращает:
        Замаскированный номер карты в формате XXXX XX** **** XXXX.
    """
    if not isinstance(card_number, int):
        logger_masks.error(f"В функцию get_mask_card_number передан нечисловой аргумент: {type(card_number)}.")
        raise TypeError("Номер карты должен быть числом.")

    card_number_str = str(card_number)
    if not card_number_str.isdigit() or len(card_number_str) != 16:
        logger_masks.error(f"Некорректный номер карты: '{card_number_str}'. Ожидается 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger_masks.info(f"Номер карты успешно замаскирован: '{masked_number}'")
    return masked_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Аргументы:
        account_number: Номер счета в виде числа.

    Возвращает:
        Замаскированный номер счета в формате **XXXX.
    """
    if not isinstance(account_number, int):
        logger_masks.error(f"В функцию get_mask_account передан нечисловой аргумент: {type(account_number)}.")
        raise TypeError("Номер счета должен быть числом.")

    account_number_str = str(account_number)
    masked_number = f"**{account_number_str[-4:]}"
    logger_masks.info(f"Номер счета успешно замаскирован: '{masked_number}'")

    return masked_number
