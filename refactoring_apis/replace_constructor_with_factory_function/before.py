class EmployeeBefore:
    def __init__(self, name: str, role_code: str) -> None:
        self.name = name
        self.role_code = role_code

        if role_code == "M":
            self.hourly_rate = 120.0
        elif role_code == "D":
            self.hourly_rate = 80.0
        elif role_code == "I":
            self.hourly_rate = 40.0
        else:
            raise ValueError("role_code is invalid")

    def monthly_salary(self, hours_worked: float) -> float:
        return round(self.hourly_rate * hours_worked, 2)
