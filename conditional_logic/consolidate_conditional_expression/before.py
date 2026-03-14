class LoanEligibilityBefore:
    def can_apply(
        self,
        age: int,
        has_overdue_debt: bool,
        is_account_suspended: bool,
        credit_score: int,
    ) -> bool:
        if age < 18:
            return False
        if has_overdue_debt:
            return False
        if is_account_suspended:
            return False
        if credit_score < 600:
            return False
        return True
