from typing import TypedDict


class Item(TypedDict):
    price: float
    quantity: int


class Customer(TypedDict):
    type: str
    country: str


class Invoice(TypedDict):
    items: list[Item]
    customer: Customer


class InvoiceProcessorAfter:

    def process_invoice(self, invoice: Invoice) -> float:
        subtotal = self.get_subtotal(invoice)
        discount = self.get_discount(invoice, subtotal)
        tax = self.get_tax(invoice, subtotal - discount)
        total = subtotal - discount + tax
        return total

    def get_subtotal(self, invoice: Invoice) -> float:
        total = 0
        for item in invoice["items"]:
            total += item["price"] * item["quantity"]
        return total

    def get_discount(self, invoice: Invoice, subtotal: float) -> float:
        if invoice["customer"]["type"] == "premium":
            return subtotal * 0.1
        return 0

    def get_tax(self, invoice: Invoice, taxable_amount: float) -> float:
        if invoice["customer"]["country"] == "BR":
            return taxable_amount * 0.12
        return taxable_amount * 0.2
