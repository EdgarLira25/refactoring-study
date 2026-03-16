import pytest

from dealing_with_inheritance.remove_subclasses.after import SubscriptionAfter
from dealing_with_inheritance.remove_subclasses.before import (
    MonthlySubscriptionBefore,
    YearlySubscriptionBefore,
)


@pytest.mark.parametrize(
    "monthly_factory",
    [
        lambda: MonthlySubscriptionBefore(customer_name="Ana"),
        lambda: SubscriptionAfter(customer_name="Ana", plan_type="monthly"),
    ],
)
def test_monthly_plan(monthly_factory):
    subscription = monthly_factory()
    assert subscription.plan_label() == "monthly"
    assert subscription.monthly_fee() == 50.0


@pytest.mark.parametrize(
    "yearly_factory",
    [
        lambda: YearlySubscriptionBefore(customer_name="Ana"),
        lambda: SubscriptionAfter(customer_name="Bia", plan_type="yearly"),
    ],
)
def test_yearly_plan(yearly_factory):
    subscription = yearly_factory()
    assert subscription.plan_label() == "yearly"
    assert subscription.monthly_fee() == 40.0
