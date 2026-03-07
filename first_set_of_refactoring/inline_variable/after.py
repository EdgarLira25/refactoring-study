from typing import TypedDict


class Item(TypedDict):
    name: str
    price: int
    quantity: int


class Order(TypedDict):
    items: list[Item]


class ShippingCalculatorAfter:

    def calculate_shipping(self, order: Order) -> float:
        return (
            0
            if sum(item["price"] * item["quantity"] for item in order["items"]) > 500
            else 20
        )
