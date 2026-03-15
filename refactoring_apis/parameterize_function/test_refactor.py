import pytest

from refactoring_apis.parameterize_function.after import CheckoutServiceAfter
from refactoring_apis.parameterize_function.before import CheckoutServiceBefore


@pytest.fixture()
def items() -> list[dict]:
    return [
        {"name": "Keyboard", "price": 300.0, "quantity": 1},
        {"name": "Mouse", "price": 100.0, "quantity": 2},
    ]


def list_checkout_services():
    return [CheckoutServiceBefore(), CheckoutServiceAfter()]


@pytest.mark.parametrize("checkout_service", list_checkout_services())
def test_final_price_for_regular(
    checkout_service: CheckoutServiceBefore | CheckoutServiceAfter,
    items: list[dict],
):
    if isinstance(checkout_service, CheckoutServiceBefore):
        price = checkout_service.final_price_for_regular(items)
    elif isinstance(checkout_service, CheckoutServiceAfter):
        price = checkout_service.final_price(items, "regular")
    assert price == 560.0


@pytest.mark.parametrize("checkout_service", list_checkout_services())
def test_final_price_for_premium(
    checkout_service: CheckoutServiceBefore | CheckoutServiceAfter,
    items: list[dict],
):
    if isinstance(checkout_service, CheckoutServiceBefore):
        price = checkout_service.final_price_for_premium(items)
    elif isinstance(checkout_service, CheckoutServiceAfter):
        price = checkout_service.final_price(items, "premium")
    assert price == 504.0
