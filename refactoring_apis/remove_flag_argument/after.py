class BookingServiceAfter:
    def booking_message_premium(self, customer_name: str) -> str:
        return f"Priority booking confirmed for {customer_name}"

    def booking_message_regular(self, customer_name: str) -> str:
        return f"Standard booking confirmed for {customer_name}"

    def delivery_days_regular(self) -> int:
        return 5

    def delivery_days_premium(self) -> int:
        return 1
