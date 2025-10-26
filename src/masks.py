def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты, показывая только первые 6 и последние 4 цифры.

    Аргументы:
        card_number: Номер карты в виде числа.

    Возвращает:
        Замаскированный номер карты в формате XXXX XX** **** XXXX.
    """

    card_number_str = str(card_number)
    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return masked_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета, показывая только последние 4 цифры.

    Аргументы:
        account_number: Номер счета в виде числа.

    Возвращает:
        Замаскированный номер счета в формате **XXXX.
    """
    account_number_str = str(account_number)
    return f"**{account_number_str[-4:]}"
