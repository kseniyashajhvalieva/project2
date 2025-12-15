from src.utils import read_json_file
from src.transactions import csv_transactions, excel_transactions
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_date
from src.search import search_by_description


def main():
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        file_path = input("Введите путь к JSON-файлу: ").strip()
        data = read_json_file(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = input("Введите путь к CSV-файлу: ").strip()
        data = csv_transactions(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = input("Введите путь к XLSX-файлу: ").strip()
        data = excel_transactions(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    # фильтрация по статусу
    while True:
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        state = input("Введите статус: ").strip().upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        print(f"Статус операции '{state}' недоступен.")

    data = filter_by_state(data, state)
    print(f"Операции отфильтрованы по статусу '{state}'")

    # сортировка
    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = order == "по убыванию"
        data = sort_by_date(data, reverse=reverse)

    # фильтр рублевых транзакций
    rub_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if rub_choice == "да":
        data = [op for op in data if op.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]

    # поиск по описанию
    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == "да":
        word = input("Введите слово для поиска: ").strip()
        data = search_by_description(data, word)

    print("Распечатываю итоговый список транзакций...")
    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}")
    for op in data:
        print(f"{get_date(op['date'])} {op['description']}")
        if 'from' in op:
            print(f"{mask_account_card(op['from'])} -> ", end="")
        print(mask_account_card(op['to']) if 'to' in op else "")
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']
        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()