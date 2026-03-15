import pytest

from refactoring_apis.replace_constructor_with_factory_function.after import (
    create_employee,
)
from refactoring_apis.replace_constructor_with_factory_function.before import (
    EmployeeBefore,
)


def list_employee_factories():
    return [EmployeeBefore, create_employee]


@pytest.mark.parametrize("employee_factory", list_employee_factories())
@pytest.mark.parametrize(
    "role_code, hours, expected",
    [
        ("M", 10, 1200.0),
        ("D", 10, 800.0),
        ("I", 10, 400.0),
    ],
)
def test_monthly_salary_by_role(
    employee_factory,
    role_code: str,
    hours: float,
    expected: float,
):
    employee = employee_factory(name="Ana", role_code=role_code)
    assert employee.monthly_salary(hours) == expected


@pytest.mark.parametrize("employee_factory", list_employee_factories())
@pytest.mark.parametrize("role_code", ["M", "D", "I"])
def test_employee_role(employee_factory, role_code: str):
    employee = employee_factory(name="Ana", role_code=role_code)
    assert employee.role_code == role_code


@pytest.mark.parametrize("employee_factory", list_employee_factories())
def test_invalid_role_code_raises_error(employee_factory):
    with pytest.raises(ValueError, match="role_code is invalid"):
        employee_factory(name="Ana", role_code="X")
