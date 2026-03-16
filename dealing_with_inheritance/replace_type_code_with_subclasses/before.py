class EmployeeBefore:
    def __init__(self, name: str, role_type: str) -> None:
        self.name = name
        self.role_type = role_type

    def hourly_rate(self) -> float:
        if self.role_type == "manager":
            return 120.0
        if self.role_type == "developer":
            return 90.0
        if self.role_type == "intern":
            return 40.0
        raise ValueError("role_type is invalid")

    def monthly_salary(self, hours_worked: float) -> float:
        return round(self.hourly_rate() * hours_worked, 2)
