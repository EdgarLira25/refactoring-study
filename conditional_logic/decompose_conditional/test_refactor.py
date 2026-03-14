import pytest

from conditional_logic.decompose_conditional.after import DeliveryFeeCalculatorAfter
from conditional_logic.decompose_conditional.before import DeliveryFeeCalculatorBefore


def list_calculator():
    return [DeliveryFeeCalculatorBefore(), DeliveryFeeCalculatorAfter()]


@pytest.mark.parametrize("calculator", list_calculator())
@pytest.mark.parametrize(
    "order_total, country, is_express, day_of_week, expected_fee",
    [
        (220.0, "BR", False, "sat", 0.0),
        (120.0, "BR", True, "mon", 35.0),
        (120.0, "US", True, "tue", 60.0),
        (120.0, "US", False, "wed", 25.0),
        (120.0, "BR", False, "fri", 15.0),
    ],
)
def test_calculate_delivery_fee(
    calculator: DeliveryFeeCalculatorBefore | DeliveryFeeCalculatorAfter,
    order_total: float,
    country: str,
    is_express: bool,
    day_of_week: str,
    expected_fee: float,
):
    fee = calculator.calculate_delivery_fee(
        order_total, country, is_express, day_of_week
    )
    assert fee == expected_fee
