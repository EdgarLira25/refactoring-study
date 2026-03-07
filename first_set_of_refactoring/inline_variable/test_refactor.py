import pytest

from first_set_of_refactoring.inline_variable.after import ShippingCalculatorAfter
from first_set_of_refactoring.inline_variable.before import ShippingCalculatorBefore


@pytest.fixture()
def order():
    return {
        "items": [
            {"name": "Laptop", "price": 3000, "quantity": 1},
            {"name": "Mouse", "price": 150, "quantity": 2},
        ]
    }


@pytest.fixture()
def order_cheap():
    return {
        "items": [
            {"name": "Laptop", "price": 2, "quantity": 1},
            {"name": "Mouse", "price": 2, "quantity": 2},
        ]
    }


@pytest.mark.parametrize(
    "shipping_calculator", [ShippingCalculatorBefore(), ShippingCalculatorAfter()]
)
def test_shipping_calculator(order: dict, shipping_calculator):
    assert shipping_calculator.calculate_shipping(order) == 0


@pytest.mark.parametrize(
    "shipping_calculator", [ShippingCalculatorBefore(), ShippingCalculatorAfter()]
)
def test_shipping_calculator_with_cheap_order(order_cheap: dict, shipping_calculator):
    assert shipping_calculator.calculate_shipping(order_cheap) == 20
