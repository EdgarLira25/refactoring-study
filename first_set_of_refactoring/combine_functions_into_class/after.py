from typing import TypedDict


class Item(TypedDict):
    price: float
    quantity: int


class OrderCalculator:
    def calculate_subtotal(self, items: list[Item]) -> float:
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        return total

    def calculate_discount(self, customer_type: str, subtotal: float) -> float:
        if customer_type == "premium":
            return subtotal * 0.1
        return 0

    def calculate_total(self, items: list[Item], customer_type: str) -> float:
        subtotal = self.calculate_subtotal(items)
        discount = self.calculate_discount(customer_type, subtotal)

        return subtotal - discount
