from typing import Literal
from abc import ABC, abstractmethod


class BonusI(ABC):

    @abstractmethod
    def calculate(self, yearly_salary: float) -> float: ...


class ManagerBonus(BonusI):
    def calculate(self, yearly_salary: float) -> float:
        return round(yearly_salary * 0.20, 2)


class EngineerBonus(BonusI):
    def calculate(self, yearly_salary: float) -> float:
        return round(yearly_salary * 0.15, 2)


class InternBonus(BonusI):
    def calculate(self, yearly_salary: float) -> float:
        return round(yearly_salary * 0.05, 2)


class AnnualBonusAfter:
    def __init__(self, employee_type: Literal["manager", "engineer", "intern"]) -> None:
        match employee_type:
            case "intern":
                self.employee = InternBonus()
            case "manager":
                self.employee = ManagerBonus()
            case "engineer":
                self.employee = EngineerBonus()
            case _:
                raise ValueError("employee_type is invalid")

    def calculate(self, yearly_salary: float) -> float:
        return self.employee.calculate(yearly_salary)
