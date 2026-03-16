class RoleAfter:
    def __init__(self, name: str, benefit_rate: float) -> None:
        self.name = name
        self.base_salary = 6000.0
        self.benefit_rate = benefit_rate

    def monthly_total(self) -> float:
        return round(self.base_salary * (1 + self.benefit_rate), 2)


class EngineerAfter(RoleAfter):
    def __init__(self, name: str) -> None:
        super().__init__(name, 0.2)


class DesignerAfter(RoleAfter):
    def __init__(self, name: str) -> None:
        super().__init__(name, 0.15)
