class TaxRateServiceAfter:
    def __init__(self, rate: float) -> None:
        self.rate = rate


class InvoiceServiceAfter:
    def __init__(self, tax_rate_service: TaxRateServiceAfter) -> None:
        self.tax_rate_service = tax_rate_service

    def total_with_tax(self, subtotal: float) -> float:
        rate = self.tax_rate_service.rate
        return round(subtotal * (1 + rate), 2)
