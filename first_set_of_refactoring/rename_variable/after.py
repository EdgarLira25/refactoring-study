from typing import TypedDict


class Item(TypedDict):
    price: float
    quantity: int


class Customer(TypedDict):
    type: str


class Order(TypedDict):
    items: list[Item]
    customer: Customer


class InvoiceCalculatorAfter:

    def calculate(self, order: Order) -> float:
        total = 0
        customer_type = order["customer"]["type"]

        for order_item in order["items"]:
            total += order_item["price"] * order_item["quantity"]

        if customer_type == "premium":
            total = total * 0.9

        return total
