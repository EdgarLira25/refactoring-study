import pytest

from dealing_with_inheritance.replace_type_code_with_subclasses.after import (
    create_employee,
)
from dealing_with_inheritance.replace_type_code_with_subclasses.before import (
    EmployeeBefore,
)


@pytest.mark.parametrize("factory", [EmployeeBefore, create_employee])
@pytest.mark.parametrize(
    "role_type, hours, expected",
    [
        ("manager", 10.0, 1200.0),
        ("developer", 10.0, 900.0),
        ("intern", 10.0, 400.0),
    ],
)
def test_monthly_salary_by_role_type(
    factory,
    role_type: str,
    hours: float,
    expected: float,
):
    employee = factory(name="Ana", role_type=role_type)
    assert employee.monthly_salary(hours) == expected


@pytest.mark.parametrize("factory", [EmployeeBefore, create_employee])
def test_invalid_role_type_raises(factory):
    with pytest.raises(ValueError, match="role_type is invalid"):
        if factory is EmployeeBefore:
            factory(name="Ana", role_type="unknown").hourly_rate()
        else:
            factory(name="Ana", role_type="unknown")
