class DiscountRateBefore:
    def __init__(self, percent: float):
        self.percent = percent

    def update_discount(self, percent: float):
        self.percent = percent


class MembershipPlanBefore:
    def __init__(self, name: str, discount_rate: float):
        self.name = name
        self.discount_rate = DiscountRateBefore(discount_rate)

    def final_price(self, base_price: float) -> float:
        return base_price * (1 - self.discount_rate.percent / 100)

    def update_discount(self, percent: float):
        self.discount_rate.update_discount(percent)

    def describe(self) -> str:
        return f"{self.name}: {self.discount_rate.percent:.0f}% off"
