from typing import Literal


class SubscriptionAfter:
    def __init__(
        self, customer_name: str, plan_type: Literal["monthly", "yearly"]
    ) -> None:
        self.customer_name = customer_name
        self.plan_type = plan_type

    def monthly_fee(self):
        return 50.0 if self.plan_type == "monthly" else 40.0

    def plan_label(self):
        return self.plan_type
