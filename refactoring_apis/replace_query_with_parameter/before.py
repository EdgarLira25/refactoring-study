class TaxRateServiceBefore:
    def __init__(self, rate: float) -> None:
        self.rate = rate

    def current_rate(self) -> float:
        return self.rate


class InvoiceServiceBefore:
    def __init__(self, tax_rate_service: TaxRateServiceBefore) -> None:
        self.tax_rate_service = tax_rate_service

    def total_with_tax(self, subtotal: float) -> float:
        rate = self.tax_rate_service.current_rate()
        return round(subtotal * (1 + rate), 2)
