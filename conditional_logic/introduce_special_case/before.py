from conditional_logic.introduce_special_case.shared import Customer


class BillingServiceBefore:
    def __init__(self, customer: Customer | None) -> None:
        self.customer = customer

    def customer_name(self) -> str:
        if self.customer is None:
            return "Guest"
        return self.customer.name

    def discount_rate(self) -> float:
        if self.customer is None:
            return 0.0
        return self.customer.discount_rate

    def can_access_priority_support(self) -> bool:
        if self.customer is None:
            return False
        return self.customer.tier in ("pro", "enterprise")

    def final_price(self, base_price: float) -> float:
        return round(base_price * (1 - self.discount_rate()), 2)
