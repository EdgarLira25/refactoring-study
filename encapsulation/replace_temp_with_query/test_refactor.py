import pytest

from encapsulation.replace_temp_with_query.after import InvoiceAfter
from encapsulation.replace_temp_with_query.before import InvoiceBefore


@pytest.fixture()
def items_with_discount():
    return [
        {"price": 600, "quantity": 1},
        {"price": 500, "quantity": 1},
    ]


@pytest.fixture()
def items_without_discount():
    return [
        {"price": 300, "quantity": 1},
        {"price": 200, "quantity": 1},
    ]


@pytest.mark.parametrize(
    "invoice",
    [
        InvoiceBefore(items=[], state="CA"),
        InvoiceAfter(items=[], state="CA"),
    ],
)
def test_total_amount_with_discount_ca(
    invoice: InvoiceBefore | InvoiceAfter, items_with_discount: list[dict]
):
    invoice.items = items_with_discount
    assert invoice.total_amount() == 1059.3


@pytest.mark.parametrize(
    "invoice",
    [
        InvoiceBefore(items=[], state="CA"),
        InvoiceAfter(items=[], state="CA"),
    ],
)
def test_tax_amount_with_discount_ca(
    invoice: InvoiceBefore | InvoiceAfter, items_with_discount: list[dict]
):
    invoice.items = items_with_discount
    assert round(invoice.tax_amount(), 2) == 69.3


@pytest.mark.parametrize(
    "invoice",
    [
        InvoiceBefore(items=[], state="NY"),
        InvoiceAfter(items=[], state="NY"),
    ],
)
def test_total_amount_without_discount_other_state(
    invoice: InvoiceBefore | InvoiceAfter, items_without_discount: list[dict]
):
    invoice.items = items_without_discount
    assert invoice.total_amount() == 560.0


@pytest.mark.parametrize(
    "invoice",
    [
        InvoiceBefore(items=[], state="NY"),
        InvoiceAfter(items=[], state="NY"),
    ],
)
def test_tax_amount_without_discount_other_state(
    invoice: InvoiceBefore | InvoiceAfter, items_without_discount: list[dict]
):
    invoice.items = items_without_discount
    assert invoice.tax_amount() == 60.0
