class InvoiceCalculatorBefore:
    def final_total(self, items: list[dict], customer_type: str) -> float:
        total = sum(item["price"] * item["quantity"] for item in items)

        if customer_type == "premium":
            total = total - (total * 0.1)

        total = total + (total * 0.12)
        return round(total, 2)
