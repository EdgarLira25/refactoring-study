from dataclasses import dataclass


@dataclass
class OrderAfter:
    total: float
    customer_tier: str

    @property
    def discount_rate(self) -> float:
        if self.customer_tier == "premium":
            return 0.1
        return 0.0


class PriceCalculatorAfter:
    def total_with_discount(self, order: OrderAfter) -> float:
        return round(order.total * (1 - order.discount_rate), 2)

    def suggested_discount_rate(self, order: OrderAfter) -> float:
        return order.discount_rate
