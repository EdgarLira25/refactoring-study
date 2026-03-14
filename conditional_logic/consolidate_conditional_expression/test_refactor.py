import pytest

from conditional_logic.consolidate_conditional_expression.after import (
    LoanEligibilityAfter,
)
from conditional_logic.consolidate_conditional_expression.before import (
    LoanEligibilityBefore,
)


def list_eligibility():
    return [LoanEligibilityBefore(), LoanEligibilityAfter()]


@pytest.mark.parametrize("eligibility", list_eligibility())
@pytest.mark.parametrize(
    "age, has_overdue_debt, is_account_suspended, credit_score, expected",
    [
        (17, False, False, 750, False),
        (28, True, False, 750, False),
        (28, False, True, 750, False),
        (28, False, False, 590, False),
        (28, False, False, 750, True),
    ],
)
def test_can_apply(
    eligibility: LoanEligibilityBefore,
    age: int,
    has_overdue_debt: bool,
    is_account_suspended: bool,
    credit_score: int,
    expected: bool,
):
    assert (
        eligibility.can_apply(
            age=age,
            has_overdue_debt=has_overdue_debt,
            is_account_suspended=is_account_suspended,
            credit_score=credit_score,
        )
        is expected
    )
