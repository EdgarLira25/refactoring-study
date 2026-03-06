from datetime import datetime
from typing import Literal, TypedDict


class Item(TypedDict):
    name: str
    category: str
    price: int
    quantity: int


class Customer(TypedDict):
    name: str
    type: str
    country: str


class Order(TypedDict):
    items: list[Item]
    customer: Customer


class OrderProccessed(TypedDict):
    items: list[Item]
    customer: Customer
    processed_at: str
    final_total: float
    priority: Literal["high", "normal"]


class OrderProcessorAfter:

    def process_order(self, order: Order) -> OrderProccessed:

        country = order["customer"]["country"]
        customer_type = order["customer"]["type"]
        total = self.calculate_total_price(order["items"])
        total = self.apply_customer_type(total, customer_type)
        shipping = self.calculate_shipping(total, country)
        tax = self.calculate_tax(total, country)
        final_total = total + shipping + tax
        order_processed = self.mark_order_as_processed(order, final_total)
        return order_processed

    def mark_order_as_processed(
        self, order: Order, final_total: float
    ) -> OrderProccessed:
        def calculate_priority():
            return "high" if final_total > 1000 else "normal"

        order_processed: dict = dict(order)
        order_processed["processed_at"] = datetime(2026, 1, 1).isoformat()
        order_processed["priority"] = calculate_priority()
        order_processed["final_total"] = final_total
        return OrderProccessed(**order_processed)

    def calculate_shipping(self, total: float, country: str):
        if total > 500:
            return 0
        return 50 if country != "BR" else 20

    def calculate_tax(self, total: float, country: str):
        if country == "BR":
            return total * 0.12
        return total * 0.20

    def calculate_total_price(self, order_items: list[Item]):
        total = 0
        for item in order_items:
            price = item["price"]
            quantity = item["quantity"]

            subtotal = price * quantity

            if item.get("category") == "electronics":
                subtotal *= 1.10

            if quantity > 10:
                subtotal *= 0.95

            total += subtotal
        return total

    def apply_customer_type(self, total: float, customer_type: str):
        if customer_type == "premium":
            total *= 0.90
        return total
