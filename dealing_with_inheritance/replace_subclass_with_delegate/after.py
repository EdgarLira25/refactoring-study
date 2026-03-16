class PremiumSupportDelegateAfter:
    def has_priority_support(self) -> bool:
        return True


class BookingAfter:
    def __init__(
        self,
        customer_name: str,
        premium_support_delegate: PremiumSupportDelegateAfter | None = None,
    ) -> None:
        self.customer_name = customer_name
        self.premium_support_delegate = premium_support_delegate

    def has_priority_support(self) -> bool:
        if self.premium_support_delegate is None:
            return False
        return self.premium_support_delegate.has_priority_support()

    def summary(self) -> str:
        if self.has_priority_support():
            return f"{self.customer_name} booking with priority support"
        return f"{self.customer_name} booking"
