import pandas as pd

def csv_transactions(file_path):
    df = pd.read_csv(file_path)
    return df.to_dict('records')


def excel_transactions(file_path):
    df = pd.read_excel(file_path)
    return df.to_dict('records')
