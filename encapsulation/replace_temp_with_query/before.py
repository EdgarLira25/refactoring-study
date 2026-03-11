class InvoiceBefore:
    def __init__(self, items: list[dict], state: str):
        self.items = items
        self.state = state

    def total_amount(self) -> float:
        subtotal = sum(item["price"] * item["quantity"] for item in self.items)
        discount = subtotal * 0.1 if subtotal > 1000 else 0
        taxable_total = subtotal - discount
        tax_rate = 0.07 if self.state == "CA" else 0.12
        tax = taxable_total * tax_rate
        total = taxable_total + tax
        return total

    def tax_amount(self) -> float:
        subtotal = sum(item["price"] * item["quantity"] for item in self.items)
        discount = subtotal * 0.1 if subtotal > 1000 else 0
        taxable_total = subtotal - discount
        tax_rate = 0.07 if self.state == "CA" else 0.12
        return taxable_total * tax_rate
