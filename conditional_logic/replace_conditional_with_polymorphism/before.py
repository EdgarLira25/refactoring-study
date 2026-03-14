class AnnualBonusBefore:
    def calculate(self, employee_type: str, yearly_salary: float) -> float:
        if employee_type == "manager":
            return round(yearly_salary * 0.20, 2)
        if employee_type == "engineer":
            return round(yearly_salary * 0.15, 2)
        if employee_type == "intern":
            return round(yearly_salary * 0.05, 2)
        raise ValueError("employee_type is invalid")
