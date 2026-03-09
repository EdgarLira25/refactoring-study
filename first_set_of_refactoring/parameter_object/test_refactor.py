import pytest
from first_set_of_refactoring.parameter_object.before import ShippingServiceBefore
from first_set_of_refactoring.parameter_object.after import (
    Shipment,
    ShippingServiceAfter,
)


@pytest.fixture()
def shipment():
    return Shipment(
        weight=10,
        width=3,
        height=5,
        depth=10,
        destination_country="BR",
    )


@pytest.mark.parametrize(
    "shipping_service", [ShippingServiceBefore(), ShippingServiceAfter()]
)
def test_invoice_calculator(
    shipment: Shipment, shipping_service: ShippingServiceBefore | ShippingServiceAfter
):
    if isinstance(shipping_service, ShippingServiceBefore):
        response = shipping_service.calculate_shipping(
            shipment.weight,
            shipment.width,
            shipment.height,
            shipment.depth,
            shipment.destination_country,
        )
    elif isinstance(shipping_service, ShippingServiceAfter):
        response = shipping_service.calculate_shipping(shipment)

    assert response == 7.15
