import pytest

from conditional_logic.introduce_special_case.after import BillingServiceAfter
from conditional_logic.introduce_special_case.before import BillingServiceBefore
from conditional_logic.introduce_special_case.shared import Customer


def list_billing_services():
    return [BillingServiceBefore, BillingServiceAfter]


@pytest.mark.parametrize("billing_service_factory", list_billing_services())
@pytest.mark.parametrize(
    "customer, expected_name, expected_discount, expected_priority_support",
    [
        (None, "Guest", 0.0, False),
        (
            Customer(name="Ana", tier="pro", discount_rate=0.1),
            "Ana",
            0.1,
            True,
        ),
        (
            Customer(name="Bia", tier="regular", discount_rate=0.03),
            "Bia",
            0.03,
            False,
        ),
    ],
)
def test_customer_behavior_by_presence(
    billing_service_factory: type[BillingServiceBefore] | type[BillingServiceAfter],
    customer: Customer | None,
    expected_name: str,
    expected_discount: float,
    expected_priority_support: bool,
):
    billing_service = billing_service_factory(customer)
    assert billing_service.customer_name() == expected_name
    assert billing_service.discount_rate() == expected_discount
    assert billing_service.can_access_priority_support() is expected_priority_support


@pytest.mark.parametrize("billing_service_factory", list_billing_services())
@pytest.mark.parametrize(
    "customer, base_price, expected",
    [
        (None, 100.0, 100.0),
        (Customer(name="Ana", tier="pro", discount_rate=0.1), 100.0, 90.0),
    ],
)
def test_final_price(
    billing_service_factory: type[BillingServiceBefore] | type[BillingServiceAfter],
    customer: Customer | None,
    base_price: float,
    expected: float,
):
    billing_service = billing_service_factory(customer)
    assert billing_service.final_price(base_price) == expected
