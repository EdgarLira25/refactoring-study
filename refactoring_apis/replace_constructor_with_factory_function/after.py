class EmployeeAfter:

    def __init__(self, name: str, role_code: str, hourly_rate: float) -> None:
        self.name = name
        self.role_code = role_code
        self.hourly_rate = hourly_rate

    def monthly_salary(self, hours_worked: float) -> float:
        return round(self.hourly_rate * hours_worked, 2)


def create_manager(name: str) -> EmployeeAfter:
    return EmployeeAfter(name=name, role_code="M", hourly_rate=120.0)


def create_designer(name: str) -> EmployeeAfter:
    return EmployeeAfter(name=name, role_code="D", hourly_rate=80.0)


def create_intern(name: str) -> EmployeeAfter:
    return EmployeeAfter(name=name, role_code="I", hourly_rate=40.0)


def create_employee(name: str, role_code: str) -> EmployeeAfter:
    if role_code == "M":
        return create_manager(name)
    if role_code == "D":
        return create_designer(name)
    if role_code == "I":
        return create_intern(name)
    raise ValueError("role_code is invalid")
