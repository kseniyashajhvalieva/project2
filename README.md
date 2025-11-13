# Виджет банковских операций клиента

Этот проект предоставляет инструменты для обработки и отображения данных о банковских операциях клиента.

## Установка

1.  Клонируйте репозиторий:
    `git clone https://github.com/kseniyashajhvalieva/project2.git`
2.  Перейдите в директорию проекта:
    `cd project2`

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

Сортирует список словарей по ключу date.

**Параметры:**
*   operations (list[dict]): Список словарей с данными о банковских операциях.
*   reverse (bool, optional): Порядок сортировки. True для убывания (по умолчанию), False для возрастания.

**Пример:**

```
sorted_operations_desc = sort_by_date(operations_data)
print(sorted_operations_desc)
# Вывод (по убыванию): [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

sorted_operations_asc = sort_by_date(operations_data, reverse=False)
print(sorted_operations_asc)
# Вывод (по возрастанию): [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```

## Тестирование
 Проект покрыт модульными тестами с использованием библиотеки pytest. Все тесты находятся в папке tests/.
Для запуска тестов используйте команду:
```
bash
pytest
```
Для генерации отчета о покрытии тестами выполните:
```
bash
pytest --cov=src --cov-report html
```
Отчет о покрытии будет доступен в папке `htmlcov/` в файле `index.html`.