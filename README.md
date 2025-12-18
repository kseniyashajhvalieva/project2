# Виджет банковских операций клиента

Этот проект предоставляет инструменты для обработки и отображения данных о банковских операциях клиента,
включая чтение транзакций из JSON-файла, их конвертацию валют и расширенное логирование.

## Новые Функции Модуля

### Чтение CSV и Excel файлов
Добавлен модуль `src/transactions.py`:
* `csv_transactions(file_path)` — читает транзакции из CSV-файла
* `excel_transactions(file_path)` — читает транзакции из Excel-файла

Функции возвращают список словарей, имеют аннотации типов и документацию.

### Чтение JSON-файла
Функция `read_json_file` (находится в `src/utils.py`) безопасно читает JSON-файл с банковскими операциями,
возвращая список словарей. Обрабатывает случаи отсутствия файла, пустого файла или некорректного JSON.

### Конвертация валют
Функция `convert_currency` (находится в `src/external_api.py`) конвертирует суммы транзакций из USD или EUR в RUB.
Для получения актуальных курсов используется внешний 
[Exchange Rates Data API](https://apilayer.com/exchangerates_data-api).

## Установка

1.  Клонируйте репозиторий:
    `git clone https://github.com/kseniyashajhvalieva/project2.git`
2.  Перейдите в директорию проекта:
    `cd project2`
3.  Установите все необходимые зависимости:
    `pip install python-dotenv requests pytest pytest-cov types-requests flake8 isort`

## Конфигурация API

Для корректной работы функции конвертации валют требуется API-ключ.
1.  Получите ваш API-ключ на [apilayer.com](https://apilayer.com/exchangerates_data-api).
2.  Создайте файл `.env` в корне проекта.
3.  Добавьте ключ в файл `.env` в формате:
    `EXCHANGE_RATE_API_KEY=ВАШ_API_КЛЮЧ`
    (Замените `ВАШ_API_КЛЮЧ` на ваш реальный ключ).
    Пример содержимого для `.env` можно найти в `example.env`.

## Использование функций

### filter_by_state

Фильтрует список словарей по значению ключа `state`.

**Параметры:**
*   `operations` (list[dict]): Список словарей с данными о банковских операциях.
*   `state` (str, optional): Значение ключа `state` для фильтрации. По умолчанию 'EXECUTED'.

**Пример:**

```
operations_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed_operations = filter_by_state(operations_data)
print(executed_operations)
# Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

canceled_operations = filter_by_state(operations_data, state='CANCELED')
print(canceled_operations)
# Вывод: [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

### sort_by_date

Сортирует список словарей по ключу `date`.

**Параметры:**
*   `operations (list[dict]):` Список словарей с данными о банковских операциях.
*   `reverse (bool, optional):` Порядок сортировки. `True` для убывания (по умолчанию), `False` для возрастания.

**Пример:**

```
sorted_operations_desc = sort_by_date(operations_data)
print(sorted_operations_desc)
# Вывод (по убыванию): [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

sorted_operations_asc = sort_by_date(operations_data, reverse=False)
print(sorted_operations_asc)
# Вывод (по возрастанию): [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

## Генераторы для обработки транзакций

Модуль `src/generators.py` содержит функции-генераторы для эффективной работы с большими объемами данных транзакций.

### filter_by_currency

Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.

**Параметры:**
* `transactions (List[Dict[str, Any]]):` Список словарей, представляющих транзакции.
* `currency (str):` Код валюты для фильтрации (например, `"USD"`, `"RUB"`).

**Пример:**
```
from src.generators import filter_by_currency

transactions = [
  {
    "id": 939719570,
    "operationAmount": {"currency": {"code": "USD"}},
    "description": "Перевод организации",
    # ... остальные поля
  },
  {
    "id": 873106923,
    "operationAmount": {"currency": {"code": "RUB"}},
    "description": "Перевод со счета на счет",
    # ... остальные поля
  },
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(1): # для получения первого элемента
  print(next(usd_transactions))
# Вывод:
# {
#  "id": 939719570,
#  "operationAmount": {"currency": {"code": "USD"}},
#  "description": "Перевод организации",
#  ...
# }
```
### transaction_descriptions
Возвращает итератор, который поочередно выдает описание каждой операции из списка транзакций.

**Параметры:**
* `transactions (List[Dict[str, Any]]):` Список словарей с транзакциями.

**Пример:**
```
from src.generators import transaction_descriptions

transactions = [
  {"description": "Перевод организации", "id": 1, ...},
  {"description": "Перевод со счета на счет", "id": 2, ...},
]

descriptions = transaction_descriptions(transactions)
for _ in range(3):
  print(next(descriptions))
# Вывод:
# Перевод организации
# Перевод со счета на счет
```
### card_number_generator

Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.

**Параметры:**
* `start (int):` Начальное значение диапазона (например, 1).
* `stop (int):` Конечное значение диапазона (например, 5).

**Пример:**
```
from src.generators import card_number_generator

for card_number in card_number_generator(1, 3):
  print(card_number)
# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
```

## Декоратор для логирования (log)

В проекте реализован универсальный декоратор `log`, предназначенный для автоматической регистрации деталей выполнения
функций. Он позволяет отслеживать вызовы функций, передаваемые аргументы, результаты выполнения и информацию о
возникающих ошибках. Логи могут быть записаны как в файл, так и выведены в консоль.

### Использование

Декоратор `log` принимает необязательный аргумент `filename`:

*   Если `filename` указан, логи будут записываться в этот файл.
*   Если `filename` не указан, логи выводятся в консоль.

**Пример:**
```
from src.decorators import log

@log(filename="mylog.txt")
def add_numbers(x: int, y: int) -> int:
    """Складывает два числа."""
    return x + y

@log()
def divide_numbers(a: int, b: int) -> float:
    """Делит одно число на другое."""
    return a / b

# Использование
add_numbers(5, 3)
# -> В mylog.txt будет записано: "add_numbers ok"

divide_numbers(10, 0)
# -> В консоль будет выведено: "divide_numbers error: ZeroDivisionError. Inputs: (10, 0), {}"
# И будет вызвано исключение ZeroDivisionError
```
## Новые функции для поиска и анализа операций

### Поиск операций по описанию
Функция `search_by_description` выполняет поиск операций по строке в описании с использованием регулярных выражений.

**Пример использования:**
```
from src.search import search_by_description

# Поиск всех операций с словом "перевод" в описании
result = search_by_description(transactions, "перевод")
```
Подсчет операций по категориям
Функция `count_by_categories` подсчитывает количество операций по заданным категориям.

**Пример использования:**
```
from src.search import count_by_categories

# Подсчет операций по категориям
categories = ["Перевод организации", "Открытие вклада"]
stats = count_by_categories(transactions, categories)
# Результат: {"Перевод организации": 5, "Открытие вклада": 3}
```
### Основной интерфейс программы
Запустите `python main.py` для работы с интерактивным меню, которое позволяет:

* Загружать данные из JSON, CSV или Excel файлов

* Фильтровать операции по статусу

* Сортировать по дате

* Отображать только рублевые транзакции

* Искать операции по ключевому слову в описании


## Тестирование
Проект покрыт модульными тестами с использованием библиотеки `pytest`, включая `unittest.mock` для изоляции внешних 
зависимостей (API-запросы, файловая система). Все тесты находятся в папке `tests/`.

* **Запуск всех тестов:** `pytest`
* **Проверка покрытия тестами (в терминале с указанием непокрытых строк):** `pytest --cov=src --cov-report=term-missing`
* **Генерация HTML-отчета о покрытии:** `pytest --cov=src --cov-report=html`
*    Отчет о покрытии будет доступен в папке `htmlcov/` в файле `index.html`.
