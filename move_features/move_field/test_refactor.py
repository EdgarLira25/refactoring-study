import pytest
from move_features.move_field.after import (
    SubscriptionSummaryAfter,
    CustomerAccountAfter,
)
from move_features.move_field.before import (
    CustomerAccountBefore,
    SubscriptionSummaryBefore,
)

type SubscriptionsSummary = SubscriptionSummaryBefore | SubscriptionSummaryAfter


def get_account_after() -> CustomerAccountAfter:
    return CustomerAccountAfter(
        customer_name="Teste", plan_name="Pro", monthly_fee=200.0, active_users=4
    )


def get_account_before() -> CustomerAccountBefore:
    return CustomerAccountBefore(
        customer_name="Teste", plan_name="Pro", monthly_fee=200.0
    )


def list_subscriptions():
    return [
        SubscriptionSummaryBefore(get_account_before(), active_users=4),
        SubscriptionSummaryAfter(get_account_after()),
    ]


@pytest.mark.parametrize("subscription_summary", list_subscriptions())
def test_per_user_cost(
    subscription_summary: SubscriptionsSummary,
):
    assert subscription_summary.per_user_cost() == 50.0


@pytest.mark.parametrize("subscription_summary", list_subscriptions())
def test_per_user_cost_with_zero_users(subscription_summary: SubscriptionsSummary):
    if isinstance(subscription_summary, SubscriptionSummaryAfter):
        subscription_summary.account.active_users = 0
    elif isinstance(subscription_summary, SubscriptionSummaryBefore):
        subscription_summary.active_users = 0
    assert subscription_summary.per_user_cost() == 0.0


@pytest.mark.parametrize("subscription_summary", list_subscriptions())
def test_summary(
    subscription_summary: SubscriptionsSummary,
):
    assert subscription_summary.summary() == "Teste on Pro: $200.00/month for 4 users"
