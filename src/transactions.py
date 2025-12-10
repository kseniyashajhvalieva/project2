import pandas as pd
from typing import List, Dict, Any

def csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """ Считывает финансовые операции из CSV"""
    df = pd.read_csv(file_path)
    return df.to_dict('records')


def excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """ Считывает финансовые операции из Excel."""
    df = pd.read_excel(file_path)
    return df.to_dict('records')
