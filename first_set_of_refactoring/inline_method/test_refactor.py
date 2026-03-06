import pytest
from first_set_of_refactoring.inline_method.after import InvoiceProcessorAfter
from first_set_of_refactoring.inline_method.before import InvoiceProcessorBefore


@pytest.fixture()
def invoice():
    return {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 3000, "quantity": 1},
            {"name": "Mouse", "category": "electronics", "price": 150, "quantity": 2},
            {"name": "Notebook", "category": "stationery", "price": 20, "quantity": 12},
        ],
        "customer": {"name": "Edgar", "type": "premium", "country": "BR"},
    }


@pytest.fixture()
def common_invoice_client():
    return {
        "items": [
            {"name": "Laptop", "category": "electronics", "price": 3000, "quantity": 1},
        ],
        "customer": {"name": "Edgar", "type": "common", "country": "BR"},
    }


@pytest.mark.parametrize(
    "invoice_processor", [InvoiceProcessorBefore(), InvoiceProcessorAfter()]
)
def test_invoice_processor(invoice: dict, invoice_processor):
    assert invoice_processor.process_invoice(invoice) == 3568.32


@pytest.mark.parametrize(
    "invoice_processor", [InvoiceProcessorBefore(), InvoiceProcessorAfter()]
)
def test_invoice_processor_with_common_client(
    common_invoice_client: dict, invoice_processor
):
    assert invoice_processor.process_invoice(common_invoice_client) == 3360.0
