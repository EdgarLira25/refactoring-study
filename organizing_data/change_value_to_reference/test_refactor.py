import pytest

from organizing_data.change_value_to_reference.after import OrderAfter, repository
from organizing_data.change_value_to_reference.before import OrderBefore
from organizing_data.change_value_to_reference.shared.customer import CustomerValue
from organizing_data.change_value_to_reference.shared.loyalty_program import (
    LoyaltyProgram,
)


@pytest.fixture(autouse=True)
def clear_repository():
    repository._customers.clear()


@pytest.fixture()
def loyalty_program() -> LoyaltyProgram:
    return LoyaltyProgram()


def get_customer():
    return CustomerValue(1, "Edgar", "regular")


def make_order_before(order_id: int, total: float) -> OrderBefore:
    return OrderBefore(order_id=order_id, customer=get_customer(), total=total)


def make_order_after(order_id: int, total: float) -> OrderAfter:
    return OrderAfter(order_id=order_id, customer=get_customer(), total=total)


@pytest.mark.parametrize("order_factory", [make_order_before, make_order_after])
def test_upgrade_sets_gold_when_eligible(
    loyalty_program: LoyaltyProgram, order_factory
):
    order = order_factory(order_id=1, total=1500.0)
    loyalty_program.upgrade_if_eligible(order)
    assert order.customer.loyalty_tier == "gold"


@pytest.mark.parametrize("order_factory", [make_order_before, make_order_after])
def test_upgrade_keeps_tier_when_not_eligible(
    loyalty_program: LoyaltyProgram, order_factory
):
    order = order_factory(order_id=1, total=999.0)
    loyalty_program.upgrade_if_eligible(order)
    assert order.customer.loyalty_tier == "regular"
