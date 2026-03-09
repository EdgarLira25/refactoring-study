import pytest
from first_set_of_refactoring.rename_variable.before import InvoiceCalculatorBefore
from first_set_of_refactoring.rename_variable.after import InvoiceCalculatorAfter


@pytest.fixture()
def order():
    return {
        "customer": {"type": "premium"},
        "items": [
            {"price": 3000, "quantity": 1},
            {"price": 150, "quantity": 2},
        ],
    }


@pytest.mark.parametrize(
    "invoice_calculator", [InvoiceCalculatorBefore(), InvoiceCalculatorAfter()]
)
def test_invoice_calculator(order: dict, invoice_calculator):
    assert invoice_calculator.calculate(order) == 2970.0
