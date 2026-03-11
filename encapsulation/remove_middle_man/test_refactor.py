import pytest

from encapsulation.remove_middle_man.after import EmployeeAfter, ExpenseApprovalAfter
from encapsulation.remove_middle_man.before import EmployeeBefore, ExpenseApprovalBefore
from encapsulation.remove_middle_man.shared import Department, Manager


def get_manager():
    return Manager(
        name="Carla", email="carla@company.com", phone="+1-555-0100", years_in_company=4
    )


def get_department():
    return Department(name="Engineering", manager=get_manager(), monthly_budget=20000.0)


def get_employee_before() -> EmployeeBefore:
    return EmployeeBefore(name="Ana", department=get_department())


def get_employee_after() -> EmployeeAfter:
    return EmployeeAfter(name="Ana", department=get_department())


type Employees = EmployeeBefore | EmployeeAfter


def list_employees():
    return [get_employee_before(), get_employee_after()]


@pytest.mark.parametrize("employee", list_employees())
def test_department_budget_delegation(employee: Employees):
    if isinstance(employee, EmployeeBefore):
        budget = employee.department_budget()
    elif isinstance(employee, EmployeeAfter):
        budget = employee.department.monthly_budget
    assert budget == 20000.0


@pytest.mark.parametrize("employee", list_employees())
@pytest.mark.parametrize(
    "amount, expected",
    [
        (1000.0, True),
        (1200.0, False),
    ],
)
def test_can_request_fast_approval(employee: Employees, amount: float, expected: bool):
    assert employee.can_request_fast_approval(amount) is expected


@pytest.mark.parametrize("employee", list_employees())
@pytest.mark.parametrize(
    "years_in_company, amount, expected_text",
    [
        (
            4,
            1000.0,
            "Fast approval by Carla (carla@company.com) for amount $1000.00",
        ),
        (
            1,
            1000.0,
            "Regular flow for amount $1000.00. Manager in charge: Carla (carla@company.com)",
        ),
    ],
)
def test_approval_summary(
    employee: Employees,
    years_in_company: int,
    amount: float,
    expected_text: str,
):
    employee.department.manager.years_in_company = years_in_company

    if isinstance(employee, EmployeeBefore):
        approval_service = ExpenseApprovalBefore(employee)
    elif isinstance(employee, EmployeeAfter):
        approval_service = ExpenseApprovalAfter(employee)

    assert approval_service.approval_summary(amount) == expected_text
