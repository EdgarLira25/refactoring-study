class ShippingServiceBefore:

    def calculate_shipping(
        self,
        weight: float,
        width: float,
        height: float,
        depth: float,
        destination_country: str,
    ) -> float:

        volume = width * height * depth

        price = weight * 0.5 + volume * 0.01

        if destination_country == "BR":
            price *= 1.1
        else:
            price *= 1.2

        return price
