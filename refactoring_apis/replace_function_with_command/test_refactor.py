import pytest

from refactoring_apis.replace_function_with_command.after import CreditScoreServiceAfter
from refactoring_apis.replace_function_with_command.before import (
    CreditScoreServiceBefore,
)


@pytest.mark.parametrize(
    "service", [CreditScoreServiceBefore(), CreditScoreServiceAfter()]
)
@pytest.mark.parametrize(
    "income, debt, late_payments, expected",
    [
        (10000.0, 2000.0, 0, 700),
        (10000.0, 4000.0, 1, 615),
        (10000.0, 7000.0, 2, 530),
        (0.0, 1000.0, 0, 580),
    ],
)
def test_calculate_score(
    service: CreditScoreServiceBefore | CreditScoreServiceAfter,
    income: float,
    debt: float,
    late_payments: int,
    expected: int,
):
    assert service.calculate_score(income, debt, late_payments) == expected
