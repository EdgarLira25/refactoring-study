import pytest

from organizing_data.change_reference_to_value.after import (
    AddressAfter,
    CustomerAfter,
    CustomerServiceAfter,
)
from organizing_data.change_reference_to_value.before import (
    AddressBefore,
    CustomerBefore,
    CustomerServiceBefore,
)


def customer_service_before():
    shared_address = AddressBefore(street="Av. Paulista", city="Sao Paulo")
    customer = CustomerBefore(name="Ana", address=shared_address)
    return CustomerServiceBefore(customer)


def customer_service_after():
    shared_address = AddressAfter(street="Av. Paulista", city="Sao Paulo")
    customer = CustomerAfter(name="Ana", address=shared_address)
    return CustomerServiceAfter(customer)


@pytest.mark.parametrize(
    "customer_service", [customer_service_before(), customer_service_after()]
)
def test_move_customer_updates_target_customer(
    customer_service: CustomerServiceBefore | CustomerServiceAfter,
):
    customer_service.move_customer(new_city="Rio")
    assert customer_service.customer.address.city == "Rio"


def test_address_equality_semantics():
    assert AddressBefore(street="A", city="B") != AddressBefore(street="A", city="B")
    assert AddressAfter(street="A", city="B") == AddressAfter(street="A", city="B")


def test_after_does_not_leak_city_change_with_shared_initial_address():
    shared_address = AddressAfter(street="Av. Paulista", city="Sao Paulo")
    ana = CustomerAfter(name="Ana", address=shared_address)
    bia = CustomerAfter(name="Bia", address=shared_address)

    service = CustomerServiceAfter(ana)
    service.move_customer(new_city="Rio")

    assert ana.address.city == "Rio"
    assert bia.address.city == "Sao Paulo"
