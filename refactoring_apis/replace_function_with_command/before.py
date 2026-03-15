class CreditScoreServiceBefore:
    def calculate_score(
        self,
        monthly_income: float,
        debt: float,
        late_payments: int,
    ) -> int:
        score = 700

        if monthly_income <= 0:
            debt_ratio = 1.0
        else:
            debt_ratio = debt / monthly_income

        if debt_ratio > 0.5:
            score -= 120
        elif debt_ratio > 0.3:
            score -= 60

        score -= late_payments * 25
        return max(300, min(850, score))
