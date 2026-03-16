import pytest

from dealing_with_inheritance.push_down_method.after import InternAfter, ManagerAfter
from dealing_with_inheritance.push_down_method.before import InternBefore, ManagerBefore


@pytest.mark.parametrize("manager_factory", [ManagerBefore, ManagerAfter])
@pytest.mark.parametrize("amount, expected", [(5000.0, True), (15000.0, False)])
def test_manager_budget_approval(manager_factory, amount: float, expected: bool):
    manager = manager_factory(name="Ana")
    assert manager.approve_budget(amount) is expected


@pytest.mark.parametrize("employee_factory", [ManagerBefore, ManagerAfter])
def test_role_manager(employee_factory):
    employee = employee_factory(name="Leo")
    assert employee.role() == "manager"


@pytest.mark.parametrize("employee_factory", [InternBefore, InternAfter])
def test_role_intern(employee_factory):
    employee = employee_factory(name="Leo")
    assert employee.role() == "intern"
