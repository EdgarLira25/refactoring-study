import pytest

from move_features.replace_inline_code_with_function_call.after import PayrollAfter
from move_features.replace_inline_code_with_function_call.before import PayrollBefore


@pytest.fixture()
def employees() -> list[dict]:
    return [
        {"name": "Ana", "salary": 5000.0},
        {"name": "Bruno", "salary": 4000.0},
    ]


@pytest.mark.parametrize("payroll", [PayrollBefore(), PayrollAfter()])
def test_monthly_report(payroll: PayrollBefore, employees: list[dict]):
    assert payroll.monthly_report(employees) == [
        {"name": "Ana", "net_salary": 4250.0},
        {"name": "Bruno", "net_salary": 3400.0},
    ]
