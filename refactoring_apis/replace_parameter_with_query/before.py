from dataclasses import dataclass


@dataclass
class OrderBefore:
    total: float
    customer_tier: str


class PriceCalculatorBefore:
    def total_with_discount(self, order: OrderBefore, discount_rate: float) -> float:
        return round(order.total * (1 - discount_rate), 2)

    def suggested_discount_rate(self, order: OrderBefore) -> float:
        if order.customer_tier == "premium":
            return 0.1
        return 0.0
