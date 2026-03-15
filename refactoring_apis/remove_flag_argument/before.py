class BookingServiceBefore:
    def booking_message(self, customer_name: str, is_premium: bool) -> str:
        if is_premium:
            return f"Priority booking confirmed for {customer_name}"
        return f"Standard booking confirmed for {customer_name}"

    def delivery_days(self, is_premium: bool) -> int:
        if is_premium:
            return 1
        return 5
