import pytest

from dealing_with_inheritance.pull_up_constructor_body.after import InvoiceAfter, ReceiptAfter
from dealing_with_inheritance.pull_up_constructor_body.before import InvoiceBefore, ReceiptBefore


@pytest.mark.parametrize("invoice_factory", [InvoiceBefore, InvoiceAfter])
def test_invoice_constructor(invoice_factory):
    invoice = invoice_factory(title="Invoice 1", total=500.0)

    assert invoice.title == "Invoice 1"
    assert invoice.status == "draft"
    assert invoice.history == []
    assert invoice.total == 500.0


@pytest.mark.parametrize("receipt_factory", [ReceiptBefore, ReceiptAfter])
def test_receipt_constructor(receipt_factory):
    receipt = receipt_factory(title="Receipt 1", paid_total=500.0)

    assert receipt.title == "Receipt 1"
    assert receipt.status == "draft"
    assert receipt.history == []
    assert receipt.paid_total == 500.0
