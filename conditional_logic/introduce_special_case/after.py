from conditional_logic.introduce_special_case.shared import Customer


class GuestCustomer:
    name = "Guest"
    discount_rate = 0.0
    tier = None


class BillingServiceAfter:
    def __init__(self, customer: Customer | None) -> None:
        self.customer = customer if customer is not None else GuestCustomer()

    def customer_name(self) -> str:
        return self.customer.name

    def discount_rate(self) -> float:
        return self.customer.discount_rate

    def can_access_priority_support(self) -> bool:
        return self.customer.tier in ("pro", "enterprise")

    def final_price(self, base_price: float) -> float:
        return round(base_price * (1 - self.discount_rate()), 2)
