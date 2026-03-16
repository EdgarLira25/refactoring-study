class Payment:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def is_valid_amount(self) -> bool:
        return self.amount > 0

    def base_processing_fee(self, fee_multiplier: float):
        return round(self.amount * fee_multiplier, 2)


class CreditCardPaymentAfter(Payment):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)

    def processing_fee(self) -> float:
        return self.base_processing_fee(0.03)


class PixPaymentAfter(Payment):
    def __init__(self, amount: float) -> None:
        super().__init__(amount)

    def processing_fee(self) -> float:
        return self.base_processing_fee(0.01)
