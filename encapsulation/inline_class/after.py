class MembershipPlanAfter:
    def __init__(self, name: str, discount_rate: float):
        self.name = name
        self.discount_rate = discount_rate

    def final_price(self, base_price: float) -> float:
        return base_price * (1 - self.discount_rate / 100)

    def update_discount_rate(self, discount_rate: float):
        self.discount_rate = discount_rate

    def describe(self) -> str:
        return f"{self.name}: {self.discount_rate:.0f}% off"
