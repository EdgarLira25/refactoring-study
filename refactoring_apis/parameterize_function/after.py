from typing import Literal


class CheckoutServiceAfter:

    def final_price(
        self, items: list[dict], customer_type: Literal["regular", "premium"]
    ) -> float:
        subtotal = sum(item["price"] * item["quantity"] for item in items)
        discount_rate = 0.1 if customer_type == "premium" else 0
        discount = subtotal * discount_rate
        subtotal -= discount
        return round(subtotal + subtotal * 0.12, 2)
