class SubscriptionBefore:
    def __init__(self, customer_name: str) -> None:
        self.customer_name = customer_name


class MonthlySubscriptionBefore(SubscriptionBefore):
    def monthly_fee(self) -> float:
        return 50.0

    def plan_label(self) -> str:
        return "monthly"


class YearlySubscriptionBefore(SubscriptionBefore):
    def monthly_fee(self) -> float:
        return 40.0

    def plan_label(self) -> str:
        return "yearly"
