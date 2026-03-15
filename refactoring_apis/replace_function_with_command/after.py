class CalculateScoreCommand:
    def __init__(self, monthly_income: float, debt: float, late_payments: int) -> None:
        self.monthly_income = monthly_income
        self.debt = debt
        self.late_payments = late_payments
        self.high_debt_ratio = 0.5
        self.medium_debt_ratio = 0.3

    @property
    def debt_ratio(self) -> float:
        return self.debt / self.monthly_income if self.monthly_income > 0 else 1

    @property
    def discounted_score(self) -> int:
        if self.debt_ratio > self.high_debt_ratio:
            return 120
        if self.debt_ratio > self.medium_debt_ratio:
            return 60
        return 0

    def execute(self) -> int:
        score = 700
        score -= self.discounted_score
        score -= self.late_payments * 25
        return max(300, min(850, score))


class CreditScoreServiceAfter:
    def calculate_score(
        self,
        monthly_income: float,
        debt: float,
        late_payments: int,
    ) -> int:
        return CalculateScoreCommand(monthly_income, debt, late_payments).execute()
