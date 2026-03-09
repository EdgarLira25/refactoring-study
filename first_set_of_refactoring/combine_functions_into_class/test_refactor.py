import pytest

from first_set_of_refactoring.combine_functions_into_class.before import (
    calculate_subtotal,
    calculate_discount,
    calculate_total,
)
from first_set_of_refactoring.combine_functions_into_class.after import OrderCalculator


@pytest.fixture()
def items():
    return [
        {"price": 3000, "quantity": 1},
        {"price": 150, "quantity": 2},
    ]


@pytest.mark.parametrize(
    "calculator",
    [
        calculate_subtotal,
        OrderCalculator().calculate_subtotal,
    ],
)
def test_calculate_subtotal(calculator, items):
    assert calculator(items) == 3300


@pytest.mark.parametrize(
    "calculator",
    [
        calculate_discount,
        OrderCalculator().calculate_discount,
    ],
)
@pytest.mark.parametrize(
    "customer_type, subtotal, expected",
    [
        ("premium", 1000, 100.0),
        ("common", 1000, 0),
    ],
)
def test_calculate_discount(calculator, customer_type, subtotal, expected):
    assert calculator(customer_type, subtotal) == expected


@pytest.mark.parametrize(
    "calculator",
    [
        calculate_total,
        OrderCalculator().calculate_total,
    ],
)
@pytest.mark.parametrize(
    "customer_type, expected",
    [
        ("premium", 2970.0),
        ("common", 3300.0),
    ],
)
def test_calculate_total(calculator, items, customer_type, expected):
    assert calculator(items, customer_type) == expected
