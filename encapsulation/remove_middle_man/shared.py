class Manager:
    def __init__(self, name: str, email: str, phone: str, years_in_company: int):
        self.name = name
        self.email = email
        self.phone = phone
        self.years_in_company = years_in_company


class Department:
    def __init__(self, name: str, manager: Manager, monthly_budget: float):
        self.name = name
        self.manager = manager
        self.monthly_budget = monthly_budget
