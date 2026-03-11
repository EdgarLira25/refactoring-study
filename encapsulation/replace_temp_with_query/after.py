class InvoiceAfter:
    def __init__(self, items: list[dict], state: str):
        self.items = items
        self.state = state

    @property
    def _subtotal(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    @property
    def _discount(self):
        return self._subtotal * 0.1 if self._subtotal > 1000 else 0

    @property
    def _taxable(self):
        return self._subtotal - self._discount

    @property
    def _tax_rate(self):
        return 0.07 if self.state == "CA" else 0.12

    def total_amount(self) -> float:
        return self._taxable + self.tax_amount()

    def tax_amount(self) -> float:
        return self._taxable * self._tax_rate
