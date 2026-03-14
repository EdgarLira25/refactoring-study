import pytest

from conditional_logic.replace_nested_conditional_with_guard_clauses.after import (
    OrderWorkflowAfter,
)
from conditional_logic.replace_nested_conditional_with_guard_clauses.before import (
    OrderWorkflowBefore,
)


def list_workflow():
    return [OrderWorkflowBefore(), OrderWorkflowAfter()]


@pytest.mark.parametrize("workflow", list_workflow())
@pytest.mark.parametrize(
    "is_canceled, is_paid, has_stock, is_address_valid, expected_step",
    [
        (True, True, True, True, "stop"),
        (False, True, True, False, "fix_address"),
        (False, True, False, True, "backorder"),
        (False, False, True, True, "await_payment"),
        (False, True, True, True, "ship"),
    ],
)
def test_next_step(
    workflow: OrderWorkflowBefore | OrderWorkflowAfter,
    is_canceled: bool,
    is_paid: bool,
    has_stock: bool,
    is_address_valid: bool,
    expected_step: str,
):
    assert (
        workflow.next_step(
            is_canceled=is_canceled,
            is_paid=is_paid,
            has_stock=has_stock,
            is_address_valid=is_address_valid,
        )
        == expected_step
    )
