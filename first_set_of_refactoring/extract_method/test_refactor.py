import pytest
from first_set_of_refactoring.extract_method.after import OrderProcessorAfter
from first_set_of_refactoring.extract_method.before import OrderProcessorBefore


@pytest.fixture()
def order_high_price():
    return {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 3000, "quantity": 1},
            {"name": "Mouse", "category": "electronics", "price": 150, "quantity": 2},
            {"name": "Notebook", "category": "stationery", "price": 20, "quantity": 12},
        ],
        "customer": {"name": "Edgar", "type": "premium", "country": "BR"},
    }


@pytest.fixture()
def order_low_price():
    return {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 30, "quantity": 1},
            {"name": "Mouse", "category": "electronics", "price": 15, "quantity": 2},
            {"name": "Notebook", "category": "stationery", "price": 20, "quantity": 12},
        ],
        "customer": {"name": "Edgar", "type": "premium", "country": "US"},
    }


@pytest.mark.parametrize(
    "order_processor", [OrderProcessorBefore(), OrderProcessorAfter()]
)
def test_order_processor_with_high_price(order_high_price: dict, order_processor):
    assert order_processor.process_order(order_high_price) == {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 3000, "quantity": 1},
            {"name": "Mouse", "category": "electronics", "price": 150, "quantity": 2},
            {"name": "Notebook", "category": "stationery", "price": 20, "quantity": 12},
        ],
        "customer": {"name": "Edgar", "type": "premium", "country": "BR"},
        "processed_at": "2026-01-01T00:00:00",
        "final_total": 3888.8640000000005,
        "priority": "high",
    }


@pytest.mark.parametrize(
    "order_processor", [OrderProcessorBefore(), OrderProcessorAfter()]
)
def test_order_processor_with_low_price(order_low_price: dict, order_processor):
    assert order_processor.process_order(order_low_price) == {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 30, "quantity": 1},
            {"name": "Mouse", "category": "electronics", "price": 15, "quantity": 2},
            {"name": "Notebook", "category": "stationery", "price": 20, "quantity": 12},
        ],
        "customer": {"name": "Edgar", "type": "premium", "country": "US"},
        "processed_at": "2026-01-01T00:00:00",
        "final_total": 367.52000000000004,
        "priority": "normal",
    }
