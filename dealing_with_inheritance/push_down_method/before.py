class EmployeeBefore:
    def __init__(self, name: str) -> None:
        self.name = name

    def approve_budget(self, amount: float) -> bool:
        return amount <= 10000.0


class ManagerBefore(EmployeeBefore):
    def role(self) -> str:
        return "manager"


class InternBefore(EmployeeBefore):
    def role(self) -> str:
        return "intern"
