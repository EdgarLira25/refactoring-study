from typing import NamedTuple


class Shipment(NamedTuple):
    weight: float
    width: float
    height: float
    depth: float
    destination_country: str


class ShippingServiceAfter:

    def calculate_shipping(self, shipment: Shipment) -> float:

        volume = shipment.width * shipment.height * shipment.depth
        price = shipment.weight * 0.5 + volume * 0.01

        if shipment.destination_country == "BR":
            price *= 1.1
        else:
            price *= 1.2

        return price
