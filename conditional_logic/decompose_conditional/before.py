class DeliveryFeeCalculatorBefore:
    def calculate_delivery_fee(
        self, order_total: float, country: str, is_express: bool, day_of_week: str
    ) -> float:
        if country == "BR" and order_total >= 200 and day_of_week in ("sat", "sun"):
            return 0.0

        if is_express:
            if country == "BR":
                return 35.0
            return 60.0

        if country == "BR":
            return 15.0
        return 25.0
