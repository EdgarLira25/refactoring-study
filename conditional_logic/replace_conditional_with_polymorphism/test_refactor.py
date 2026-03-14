from typing import Literal
import pytest

from conditional_logic.replace_conditional_with_polymorphism.after import (
    AnnualBonusAfter,
)
from conditional_logic.replace_conditional_with_polymorphism.before import (
    AnnualBonusBefore,
)


def list_bonus_calculators():
    return [AnnualBonusBefore, AnnualBonusAfter]


@pytest.mark.parametrize("bonus_calculator", list_bonus_calculators())
@pytest.mark.parametrize(
    "employee_type, yearly_salary, expected_bonus",
    [
        ("manager", 120000.0, 24000.0),
        ("engineer", 120000.0, 18000.0),
        ("intern", 48000.0, 2400.0),
    ],
)
def test_calculate_bonus_by_employee_type(
    bonus_calculator: type[AnnualBonusBefore] | type[AnnualBonusAfter],
    employee_type: Literal["manager", "engineer", "intern"],
    yearly_salary: float,
    expected_bonus: float,
):
    if bonus_calculator is AnnualBonusBefore:
        calculator = bonus_calculator()
        bonus = calculator.calculate(
            employee_type=employee_type,
            yearly_salary=yearly_salary,
        )
    elif bonus_calculator is AnnualBonusAfter:
        calculator = bonus_calculator(employee_type)
        bonus = calculator.calculate(yearly_salary=yearly_salary)
    else:
        raise AssertionError("unexpected calculator")

    assert bonus == expected_bonus


@pytest.mark.parametrize("bonus_calculator", list_bonus_calculators())
def test_calculate_bonus_raises_for_invalid_employee_type(
    bonus_calculator: type[AnnualBonusBefore] | type[AnnualBonusAfter],
):
    with pytest.raises(ValueError, match="employee_type is invalid"):
        if bonus_calculator is AnnualBonusBefore:
            bonus_calculator().calculate(
                employee_type="contractor",
                yearly_salary=90000.0,
            )
        elif bonus_calculator is AnnualBonusAfter:
            bonus_calculator(employee_type="contractor")
