class LoanEligibilityAfter:
    def can_apply(
        self,
        age: int,
        has_overdue_debt: bool,
        is_account_suspended: bool,
        credit_score: int,
    ) -> bool:
        if age < 18 or has_overdue_debt or is_account_suspended or credit_score < 600:
            return False
        return True
