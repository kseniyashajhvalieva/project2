import csv

def csv_transactions(file_path):
    transactions = []
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            transactions.append(row)
    return transactions
