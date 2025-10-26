from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета."""
    if "Счет" in data:
        return get_mask_account(int(data.split()[-1]))
    else:
        return get_mask_card_number(int(data.split()[-1]))