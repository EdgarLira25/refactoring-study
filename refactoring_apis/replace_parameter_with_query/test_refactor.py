import pytest

from refactoring_apis.replace_parameter_with_query.after import (
    OrderAfter,
    PriceCalculatorAfter,
)
from refactoring_apis.replace_parameter_with_query.before import (
    OrderBefore,
    PriceCalculatorBefore,
)


def list_calculators():
    return [PriceCalculatorBefore(), PriceCalculatorAfter()]


@pytest.mark.parametrize("calculator", list_calculators())
@pytest.mark.parametrize(
    "order_dict, discount_rate, expected",
    [
        ({"total": 200.0, "customer_tier": "premium"}, 0.1, 180.0),
        ({"total": 200.0, "customer_tier": "regular"}, 0.0, 200.0),
    ],
)
def test_total_with_discount(
    calculator: PriceCalculatorBefore | PriceCalculatorAfter,
    order_dict: dict,
    discount_rate: float,
    expected: float,
):
    if isinstance(calculator, PriceCalculatorBefore):
        result = calculator.total_with_discount(
            OrderBefore(**order_dict), discount_rate
        )
    elif isinstance(calculator, PriceCalculatorAfter):
        result = calculator.total_with_discount(OrderAfter(**order_dict))

    assert result == expected


@pytest.mark.parametrize("calculator", list_calculators())
@pytest.mark.parametrize(
    "order_dict, expected_rate",
    [
        ({"total": 100.0, "customer_tier": "premium"}, 0.1),
        ({"total": 100.0, "customer_tier": "regular"}, 0.0),
    ],
)
def test_suggested_discount_rate(
    calculator: PriceCalculatorBefore | PriceCalculatorAfter,
    order_dict: dict,
    expected_rate: float,
):
    if isinstance(calculator, PriceCalculatorBefore):
        rate = calculator.suggested_discount_rate(OrderBefore(**order_dict))
    elif isinstance(calculator, PriceCalculatorAfter):
        rate = calculator.suggested_discount_rate(OrderAfter(**order_dict))

    assert rate == expected_rate
