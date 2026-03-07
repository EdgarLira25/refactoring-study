import pytest

from first_set_of_refactoring.change_function_declaration.after import OrderServiceAfter
from first_set_of_refactoring.change_function_declaration.before import (
    OrderServiceBefore,
)


@pytest.fixture()
def order():
    return {
        "items": [
            {"name": "Laptop", "price": 3000, "quantity": 1},
            {"name": "Mouse", "price": 150, "quantity": 2},
        ],
        "customer": {"type": "premium", "email": "edgar@email.com"},
    }


@pytest.mark.parametrize("order_processor", [OrderServiceBefore(), OrderServiceAfter()])
def test_order_service(order: dict, order_processor):
    order_processed = order_processor.process(order)
    assert order_processed == {
        "customer": {"email": "edgar@email.com", "type": "premium"},
        "items": [
            {"name": "Laptop", "price": 3000, "quantity": 1},
            {"name": "Mouse", "price": 150, "quantity": 2},
        ],
        "total": 2970.0,
    }
