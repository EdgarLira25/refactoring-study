import pytest

from first_set_of_refactoring.combine_function_into_transform.after.after import (
    Client1After,
    Client2After,
    Client3After,
)
from first_set_of_refactoring.combine_function_into_transform.after.enrich_order import (
    EnrichOrder,
)
from first_set_of_refactoring.combine_function_into_transform.before.before import (
    Client1Before,
    Client2Before,
    Client3Before,
)


@pytest.fixture()
def order():
    return {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 3000, "quantity": 1},
            {"name": "Mouse", "category": "electronics", "price": 150, "quantity": 2},
            {"name": "Notebook", "category": "stationery", "price": 20, "quantity": 12},
        ],
        "customer_type": "premium",
    }


@pytest.mark.parametrize("client1", [Client1Before(), Client1After(EnrichOrder())])
def test_client_1(order: dict, client1):
    result = client1.random_example(order)

    assert result == {
        "subtotal": 3540,
        "total_items": 15,
    }


@pytest.mark.parametrize("client2", [Client2Before(), Client2After(EnrichOrder())])
def test_client_2(order: dict, client2):
    result = client2.random_example(order)

    assert result == {
        "subtotal": 3540,
        "discount": 354.0,
    }


@pytest.mark.parametrize("client3", [Client3Before(), Client3After(EnrichOrder())])
def test_client_3(order: dict, client3):
    result = client3.random_example(order)

    assert result == {
        "tax": 424.8,
        "total": 3610.8,
    }
