from typing import TypedDict


class Item(TypedDict):
    price: float
    quantity: int


class Customer(TypedDict):
    type: str
    email: str


class Order(TypedDict):
    items: list[Item]
    customer: Customer


class OrderProcessed(TypedDict):
    items: list[Item]
    customer: Customer
    total: float


class OrderServiceAfter:

    def process(self, order: Order) -> OrderProcessed:
        total = self.calc_total_price(order["items"])
        discount = self.calc_discount(order["customer"]["type"], total)
        final_total = total - discount
        self.notify_via_email(order["customer"]["email"], final_total, order["items"])
        order_processed = OrderProcessed(**order, total=final_total)
        return order_processed

    def calc_total_price(self, items: list[Item]) -> float:
        total = 0
        for item in items:
            total += item["price"] * item["quantity"]
        return total

    def calc_discount(self, customer_type: str, total: float) -> float:
        if customer_type == "premium":
            return total * 0.1
        return 0

    def notify_via_email(self, email: str, total: float, order_items: list[Item]):
        # notifying...
        return f"Sending email to {email} with total {total}, {order_items}"
