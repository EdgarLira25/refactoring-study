from typing import Literal


class EmployeeAfter:
    def __init__(self, name: str, role_type: str, hourly_rate: float) -> None:
        self.name = name
        self.role_type = role_type
        self.hourly_rate = hourly_rate

    def monthly_salary(self, hours_worked: float) -> float:
        return round(self.hourly_rate * hours_worked, 2)


class ManagerAfter(EmployeeAfter):
    def __init__(self, name: str) -> None:
        super().__init__(name, "manager", 120.0)


class DeveloperAfter(EmployeeAfter):
    def __init__(self, name: str) -> None:
        super().__init__(name, "developer", 90.0)


class InternAfter(EmployeeAfter):
    def __init__(self, name: str) -> None:
        super().__init__(name, "intern", 40.0)


def create_employee(name: str, role_type: Literal["manager", "developer", "intern"]):
    match role_type:
        case "developer":
            return DeveloperAfter(name)
        case "intern":
            return InternAfter(name)
        case "manager":
            return ManagerAfter(name)
    raise ValueError("role_type is invalid")
