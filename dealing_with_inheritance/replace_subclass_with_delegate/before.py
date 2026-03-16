class BookingBefore:
    def __init__(self, customer_name: str) -> None:
        self.customer_name = customer_name

    def has_priority_support(self) -> bool:
        return False

    def summary(self) -> str:
        if self.has_priority_support():
            return f"{self.customer_name} booking with priority support"
        return f"{self.customer_name} booking"


class PremiumBookingBefore(BookingBefore):
    def has_priority_support(self) -> bool:
        return True
