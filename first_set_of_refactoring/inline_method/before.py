class InvoiceProcessorBefore:

    def process_invoice(self, invoice: dict) -> float:
        subtotal = self.get_subtotal(invoice)
        discount = self.get_discount(invoice, subtotal)
        tax = self.get_tax(invoice, subtotal - discount)
        total = self.sum_total(subtotal, discount, tax)
        return total

    def get_subtotal(self, invoice: dict) -> float:
        return self.sum_items(invoice["items"])

    def sum_items(self, items: list[dict]) -> float:
        total = 0
        for item in items:
            total += self.multiply_price_quantity(item)
        return total

    def multiply_price_quantity(self, item: dict) -> float:
        return item["price"] * item["quantity"]

    def get_discount(self, invoice: dict, subtotal: float) -> float:
        if self.is_premium_customer(invoice):
            return self.calculate_premium_discount(subtotal)
        return 0

    def is_premium_customer(self, invoice: dict) -> bool:
        return invoice["customer"]["type"] == "premium"

    def calculate_premium_discount(self, subtotal: float) -> float:
        return subtotal * 0.1

    def get_tax(self, invoice: dict, taxable_amount: float) -> float:
        if self.is_br_customer(invoice):
            return self.calculate_br_tax(taxable_amount)
        return self.calculate_default_tax(taxable_amount)

    def is_br_customer(self, invoice: dict) -> bool:
        return invoice["customer"]["country"] == "BR"

    def calculate_br_tax(self, amount: float) -> float:
        return amount * 0.12

    def calculate_default_tax(self, amount: float) -> float:
        return amount * 0.2

    def sum_total(self, subtotal: float, discount: float, tax: float) -> float:
        return subtotal - discount + tax
