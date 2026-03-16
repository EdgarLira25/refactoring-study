class FinancialDocumentBefore:
    def __init__(self, title: str) -> None:
        self.title = title


class InvoiceBefore(FinancialDocumentBefore):
    def __init__(self, title: str, total: float) -> None:
        super().__init__(title)
        self.status = "draft"
        self.history = []
        self.total = total


class ReceiptBefore(FinancialDocumentBefore):
    def __init__(self, title: str, paid_total: float) -> None:
        super().__init__(title)
        self.status = "draft"
        self.history = []
        self.paid_total = paid_total
