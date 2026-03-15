import pytest

from refactoring_apis.replace_query_with_parameter.after import (
    InvoiceServiceAfter,
    TaxRateServiceAfter,
)
from refactoring_apis.replace_query_with_parameter.before import (
    InvoiceServiceBefore,
    TaxRateServiceBefore,
)


def list_service_factories():
    return [InvoiceServiceBefore, InvoiceServiceAfter]


@pytest.mark.parametrize("invoice_factory", list_service_factories())
@pytest.mark.parametrize(
    "rate, subtotal, expected",
    [
        (0.12, 100.0, 112.0),
        (0.05, 100.0, 105.0),
    ],
)
def test_total_with_tax(
    invoice_factory: type[InvoiceServiceBefore] | type[InvoiceServiceAfter],
    rate: float,
    subtotal: float,
    expected: float,
):
    if invoice_factory is InvoiceServiceBefore:
        invoice_service = invoice_factory(TaxRateServiceBefore(rate=rate))
    elif invoice_factory is InvoiceServiceAfter:
        invoice_service = invoice_factory(TaxRateServiceAfter(rate=rate))
    else:
        raise AssertionError("Invalid Invoice")

    assert invoice_service.total_with_tax(subtotal) == expected


@pytest.mark.parametrize("invoice_factory", list_service_factories())
@pytest.mark.parametrize(
    "rate, subtotal, expected_total", [(0.1, 100, 110), (0.2, 100, 120)]
)
def test_total_with_tax_reflects_service_state_change(
    invoice_factory: type[InvoiceServiceBefore] | type[InvoiceServiceAfter],
    rate: float,
    subtotal: float,
    expected_total: float,
):
    if invoice_factory is InvoiceServiceBefore:
        invoice_service = invoice_factory(TaxRateServiceBefore(rate=rate))
    elif invoice_factory is InvoiceServiceAfter:
        invoice_service = invoice_factory(TaxRateServiceAfter(rate=rate))
    else:
        raise AssertionError("Invalid Invoice")

    total = invoice_service.total_with_tax(subtotal)
    assert total == expected_total
