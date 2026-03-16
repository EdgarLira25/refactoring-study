class RoleBefore:
    ...

class EngineerBefore(RoleBefore):
    def __init__(self, name: str) -> None:
        self.name = name
        self.base_salary = 6000.0
        self.benefit_rate = 0.2

    def monthly_total(self) -> float:
        return round(self.base_salary * (1 + self.benefit_rate), 2)


class DesignerBefore(RoleBefore):
    def __init__(self, name: str) -> None:
        self.name = name
        self.base_salary = 6000.0
        self.benefit_rate = 0.15

    def monthly_total(self) -> float:
        return round(self.base_salary * (1 + self.benefit_rate), 2)
