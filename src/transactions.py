from typing import Any, Dict, cast

import pandas as pd


def csv_transactions(file_path: str) -> list[Dict[str, Any]]:
    """Считывает финансовые операции из CSV"""
    df = pd.read_csv(file_path)
    return cast(list[Dict[str, Any]], df.to_dict("records"))


def excel_transactions(file_path: str) -> list[Dict[str, Any]]:
    """Считывает финансовые операции из Excel."""
    df = pd.read_excel(file_path)
    return cast(list[Dict[str, Any]], df.to_dict("records"))
