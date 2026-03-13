class CustomerAccountAfter:
    def __init__(
        self, customer_name: str, plan_name: str, monthly_fee: float, active_users: int
    ):
        self.customer_name = customer_name
        self.plan_name = plan_name
        self.monthly_fee = monthly_fee
        self.active_users = active_users


class SubscriptionSummaryAfter:
    def __init__(self, account: CustomerAccountAfter):
        self.account = account

    def per_user_cost(self) -> float:
        if self.account.active_users == 0:
            return 0.0
        return self.account.monthly_fee / self.account.active_users

    def summary(self) -> str:
        return (
            f"{self.account.customer_name} on {self.account.plan_name}: "
            f"${self.account.monthly_fee:.2f}/month for {self.account.active_users} users"
        )
