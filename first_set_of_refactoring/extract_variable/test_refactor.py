import pytest
from first_set_of_refactoring.extract_variable.after import SubscriptionBillingAfter
from first_set_of_refactoring.extract_variable.before import SubscriptionBillingBefore


@pytest.fixture()
def subscription_pro():
    return {"plan": "pro", "users": 8, "projects": 15, "country": "BR"}


@pytest.fixture()
def subscription_common():
    return {"plan": "common", "users": 5, "projects": 5, "country": "US"}


@pytest.mark.parametrize(
    "billing", [SubscriptionBillingBefore(), SubscriptionBillingAfter()]
)
def test_subscription_pro(subscription_pro: dict, billing):
    assert billing.calculate_monthly_price(subscription_pro) == 145.15200000000002


@pytest.mark.parametrize(
    "billing", [SubscriptionBillingBefore(), SubscriptionBillingAfter()]
)
def test_subscription_common(subscription_common: dict, billing):
    assert billing.calculate_monthly_price(subscription_common) == 63.0
