import pytest

from encapsulation.inline_class.after import MembershipPlanAfter
from encapsulation.inline_class.before import MembershipPlanBefore


def get_membership_plan_before():
    return MembershipPlanBefore(name="Premium", discount_rate=10.0)


def get_membership_plan_after():
    return MembershipPlanAfter(name="Premium", discount_rate=10.0)


type Plans = MembershipPlanAfter | MembershipPlanBefore


def list_membership_plans():
    return [get_membership_plan_before(), get_membership_plan_after()]


@pytest.mark.parametrize("plan", list_membership_plans())
@pytest.mark.parametrize(
    "base_price, expected_final_price",
    [
        (200.0, 180.0),
        (80.0, 72.0),
    ],
)
def test_final_price(plan: Plans, base_price: float, expected_final_price: float):
    assert plan.final_price(base_price) == expected_final_price


@pytest.mark.parametrize("plan", list_membership_plans())
def test_update_discount(plan: Plans):
    if isinstance(plan, MembershipPlanBefore):
        plan.update_discount(15.0)
        discount_rate = plan.discount_rate.percent
    elif isinstance(plan, MembershipPlanAfter):
        plan.update_discount_rate(15.0)
        discount_rate = plan.discount_rate

    assert discount_rate == 15.0
    assert plan.final_price(200.0) == 170.0


@pytest.mark.parametrize("plan", list_membership_plans())
def test_describe(plan: Plans):
    assert plan.describe() == "Premium: 10% off"


@pytest.mark.parametrize("plan", list_membership_plans())
def test_describe_after_discount_update(plan: Plans):
    if isinstance(plan, MembershipPlanBefore):
        plan.update_discount(25.0)
    elif isinstance(plan, MembershipPlanAfter):
        plan.update_discount_rate(25.0)

    assert plan.describe() == "Premium: 25% off"
