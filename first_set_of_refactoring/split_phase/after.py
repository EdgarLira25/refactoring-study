from typing import NamedTuple


class ParsedOrder(NamedTuple):
    product: str
    quantity: int
    price: float


class OrderProcessorAfter:

    def process(self, order: str) -> float:
        order_parsed = self.parse_order(order)

        subtotal = order_parsed.quantity * order_parsed.price

        if order_parsed.product == "laptop":
            subtotal *= 0.9

        tax = subtotal * 0.12

        return subtotal + tax

    def parse_order(self, order: str) -> ParsedOrder:
        parts = order.split(",")
        product = parts[0]
        quantity = int(parts[1])
        price = float(parts[2])
        return ParsedOrder(product=product, quantity=quantity, price=price)
