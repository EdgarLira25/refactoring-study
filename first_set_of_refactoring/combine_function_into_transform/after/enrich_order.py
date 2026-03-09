from typing import NamedTuple


class EnrichedOrder(NamedTuple):
    subtotal_price: float
    total_items: float
    discount: float
    tax: float
    total_price: float


class EnrichOrder:

    def enrich_order(self, order: dict) -> EnrichedOrder:
        return EnrichedOrder(
            subtotal_price=self._calculate_subtotal(order),
            discount=self._calculate_discount(order),
            tax=self._calculate_tax(order),
            total_items=self._calculate_total_items(order),
            total_price=self._calculate_total(order),
        )

    def _calculate_subtotal(self, order: dict) -> float:
        subtotal = 0
        for item in order["items"]:
            subtotal += item["price"] * item["quantity"]
        return subtotal

    def _calculate_total_items(self, order: dict) -> int:
        total = 0
        for item in order["items"]:
            total += item["quantity"]
        return total

    def _calculate_discount(self, order: dict) -> float:
        subtotal = self._calculate_subtotal(order)
        if order["customer_type"] == "premium":
            return subtotal * 0.1
        return 0

    def _calculate_tax(self, order: dict) -> float:
        subtotal = self._calculate_subtotal(order)
        return subtotal * 0.12

    def _calculate_total(self, order: dict) -> float:
        subtotal = self._calculate_subtotal(order)
        discount = self._calculate_discount(order)
        tax = self._calculate_tax(order)

        return subtotal - discount + tax
