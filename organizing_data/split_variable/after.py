class InvoiceCalculatorAfter:
    def final_total(self, items: list[dict], customer_type: str) -> float:
        total_price = sum(item["price"] * item["quantity"] for item in items)
        discount = total_price * 0.1 if customer_type == "premium" else 0
        total_price_with_discount = total_price - discount
        tax = total_price_with_discount * 0.12
        total = total_price_with_discount + tax
        return round(total, 2)
