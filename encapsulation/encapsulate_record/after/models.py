from dataclasses import dataclass
from typing import Literal


@dataclass
class Item:
    name: str
    price: float
    quantity: float


@dataclass
class Customer:
    name: str
    email: str
    type: Literal["regular", "premium"]
    country: str

    def update_customer_type(self, type: Literal["regular", "premium"]):
        self.type = type


@dataclass
class Order:
    id: int
    status: Literal["completed", "pending", "processed"]
    items: list[Item]
    customer: Customer
    total: float

    def update_order_status(self, status: Literal["completed", "pending", "processed"]):
        self.status = status

    def apply_discount(self, total: float):
        self.total *= total

    @staticmethod
    def from_dict(order: dict) -> Order:
        items = [
            Item(name=item["name"], price=item["price"], quantity=item["quantity"])
            for item in order["items"]
        ]
        customer_dict = order["customer"]
        customer = Customer(
            name=customer_dict["name"],
            email=customer_dict["email"],
            type=customer_dict["type"],
            country=customer_dict["country"],
        )
        return Order(
            id=order["id"],
            status=order["status"],
            items=items,
            customer=customer,
            total=order["total"],
        )
