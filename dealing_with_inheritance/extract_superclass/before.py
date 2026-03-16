class CreditCardPaymentBefore:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def is_valid_amount(self) -> bool:
        return self.amount > 0

    def processing_fee(self) -> float:
        return round(self.amount * 0.03, 2)


class PixPaymentBefore:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def is_valid_amount(self) -> bool:
        return self.amount > 0

    def processing_fee(self) -> float:
        return round(self.amount * 0.01, 2)
