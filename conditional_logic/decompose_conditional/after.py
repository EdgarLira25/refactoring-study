class DeliveryFeeCalculatorAfter:
    def _is_from_brazil(self, country: str):
        return country == "BR"

    def _is_delivery_free(self, order_total: float, country: str, day_of_week: str):
        return (
            self._is_from_brazil(country)
            and order_total >= 200
            and day_of_week in ("sat", "sun")
        )

    def calculate_delivery_fee(
        self, order_total: float, country: str, is_express: bool, day_of_week: str
    ) -> float:
        if self._is_delivery_free(order_total, country, day_of_week):
            return 0.0

        if is_express:
            if self._is_from_brazil(country):
                return 35.0
            return 60.0

        if self._is_from_brazil(country):
            return 15.0
        return 25.0
