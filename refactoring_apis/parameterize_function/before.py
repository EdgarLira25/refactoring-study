class CheckoutServiceBefore:
    def subtotal(self, items: list[dict]) -> float:
        return sum(item["price"] * item["quantity"] for item in items)

    def final_price_for_regular(self, items: list[dict]) -> float:
        subtotal = self.subtotal(items)
        return round(subtotal + (subtotal * 0.12), 2)

    def final_price_for_premium(self, items: list[dict]) -> float:
        subtotal = self.subtotal(items)
        subtotal_with_discount = subtotal - (subtotal * 0.1)
        return round(subtotal_with_discount + (subtotal_with_discount * 0.12), 2)
