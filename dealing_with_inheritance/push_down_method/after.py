class EmployeeAfter:
    def __init__(self, name: str) -> None:
        self.name = name


class ManagerAfter(EmployeeAfter):
    def role(self) -> str:
        return "manager"

    def approve_budget(self, amount: float) -> bool:
        return amount <= 10000.0

class InternAfter(EmployeeAfter):
    def role(self) -> str:
        return "intern"


