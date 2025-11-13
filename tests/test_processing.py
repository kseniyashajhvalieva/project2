import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T10:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-05T12:00:00.000000'},
        {'id': 3, 'state': 'PENDING', 'date': '2023-01-03T09:00:00.000000'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-01-02T11:00:00.000000'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-01-04T13:00:00.000000'}
    ]

@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 4, 5]),
    ("CANCELED", [2]),
    ("PENDING", [3]),
    ("NONEXISTENT", [])
])
def test_filter_by_state(sample_operations, state, expected_ids):
    filtered_ops = filter_by_state(sample_operations, state)
    actual_ids = [op['id'] for op in filtered_ops]
    assert sorted(actual_ids) == sorted(expected_ids)

def test_filter_by_state_empty_list():
    assert filter_by_state([], "EXECUTED") == []

@pytest.mark.parametrize("reverse, expected_ids_order", [
    (True, [2, 5, 3, 4, 1]),  # От новых к старым (2023-01-05, 2023-01-04, 2023-01-03, 2023-01-02, 2023-01-01)
    (False, [1, 4, 3, 5, 2]) # От старых к новым (2023-01-01, 2023-01-02, 2023-01-03, 2023-01-04, 2023-01-05)
])
def test_sort_by_date(sample_operations, reverse, expected_ids_order):
    sorted_ops = sort_by_date(sample_operations, reverse=reverse)
    actual_ids_order = [op['id'] for op in sorted_ops]
    assert actual_ids_order == expected_ids_order

def test_sort_by_date_empty_list():
    assert sort_by_date([]) == []

def test_sort_by_date_missing_date_key():
    operations_with_missing_date = [
        {'id': 10, 'state': 'EXECUTED', 'date': '2023-01-10T00:00:00.000000'},
        {'id': 11, 'state': 'EXECUTED'}, # Отсутствует ключ 'date'
        {'id': 12, 'state': 'EXECUTED', 'date': '2023-01-09T00:00:00.000000'}
    ]
    sorted_ops = sort_by_date(operations_with_missing_date, reverse=True)
    # Ожидаем, что операции без даты будут в самом конце при reverse=True (используется "1970-01-01" как дефолт)
    # или в самом начале при reverse=False
    actual_ids_order = [op['id'] for op in sorted_ops]
    assert actual_ids_order == [10, 12, 11] # 11 в конце из-за дефолтной даты

    sorted_ops_asc = sort_by_date(operations_with_missing_date, reverse=False)
    actual_ids_order_asc = [op['id'] for op in sorted_ops_asc]
    assert actual_ids_order_asc == [11, 12, 10] # 11 в начале
