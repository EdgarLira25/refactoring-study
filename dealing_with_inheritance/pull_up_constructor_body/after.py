class FinancialDocumentAfter:
    def __init__(self, title: str) -> None:
        self.title = title
        self.status = "draft"
        self.history = []

class InvoiceAfter(FinancialDocumentAfter):
    def __init__(self, title: str, total: float) -> None:
        super().__init__(title)
        self.total = total


class ReceiptAfter(FinancialDocumentAfter):
    def __init__(self, title: str, paid_total: float) -> None:
        super().__init__(title)
        self.paid_total = paid_total
