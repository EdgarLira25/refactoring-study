import pytest

from organizing_data.split_variable.after import InvoiceCalculatorAfter
from organizing_data.split_variable.before import InvoiceCalculatorBefore


def list_calculator():
    return [InvoiceCalculatorBefore(), InvoiceCalculatorAfter()]


@pytest.fixture()
def items() -> list[dict]:
    return [
        {"name": "Laptop", "price": 3000.0, "quantity": 1},
        {"name": "Mouse", "price": 200.0, "quantity": 1},
    ]


@pytest.mark.parametrize("calculator", list_calculator())
@pytest.mark.parametrize(
    "customer_type, expected_total",
    [
        ("premium", 3225.6),
        ("regular", 3584.0),
    ],
)
def test_final_total(
    calculator: InvoiceCalculatorBefore | InvoiceCalculatorAfter,
    items: list[dict],
    customer_type: str,
    expected_total: float,
):
    assert calculator.final_total(items, customer_type) == expected_total
