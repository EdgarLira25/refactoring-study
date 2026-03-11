import pytest

from encapsulation.hide_delegate.after import (
    NotificationServiceAfter,
    OrderAfter,
    ShippingServiceAfter,
)
from encapsulation.hide_delegate.before import (
    NotificationServiceBefore,
    OrderBefore,
    ShippingServiceBefore,
)
from encapsulation.hide_delegate.shared import Address, Customer


def get_address():
    return Address(
        street="Rua Teste, 123",
        city="Seattle",
        state="NY",
        country="US",
    )


def get_customer(
    customer_name: str = "Ana",
    customer_email: str = "ana@email.com",
):
    return Customer(
        name=customer_name,
        email=customer_email,
        address=get_address(),
    )


def make_order_before(
    country: str = "US",
    state: str = "NY",
    city: str = "Seattle",
    order_id: int = 1,
    customer_name: str = "Ana",
    customer_email: str = "ana@email.com",
) -> OrderBefore:
    customer = get_customer(customer_name=customer_name, customer_email=customer_email)
    customer.address.country = country
    customer.address.state = state
    customer.address.city = city
    return OrderBefore(order_id=order_id, customer=customer, total=330.0)


def make_order_after(
    country: str = "US",
    state: str = "NY",
    city: str = "Seattle",
    order_id: int = 1,
    customer_name: str = "Ana",
    customer_email: str = "ana@email.com",
) -> OrderAfter:
    customer = get_customer(customer_name=customer_name, customer_email=customer_email)
    customer.address.country = country
    customer.address.state = state
    customer.address.city = city
    return OrderAfter(order_id=order_id, customer=customer, total=330.0)


def make_shipping_service_before(country: str, state: str):
    return ShippingServiceBefore(make_order_before(country=country, state=state))


def make_shipping_service_after(country: str, state: str):
    return ShippingServiceAfter(make_order_after(country=country, state=state))


def list_shipping_service_factories():
    return [
        make_shipping_service_before,
        make_shipping_service_after,
    ]


def list_notification_service():
    return [
        NotificationServiceBefore(make_order_before()),
        NotificationServiceAfter(make_order_after()),
    ]


@pytest.mark.parametrize("shipping_service_factory", list_shipping_service_factories())
@pytest.mark.parametrize(
    "country, state, expected_zone",
    [
        ("BR", "SP", "INTL"),
        ("US", "CA", "WEST"),
        ("US", "NY", "STANDARD"),
    ],
)
def test_shipping_zone(
    shipping_service_factory, country: str, state: str, expected_zone: str
):
    shipping_service = shipping_service_factory(country=country, state=state)
    assert shipping_service.shipping_zone() == expected_zone


@pytest.mark.parametrize(
    "notification_service",
    list_notification_service(),
)
def test_delivery_message(notification_service):
    message = notification_service.delivery_message(eta_days=3)
    assert message == (
        "Hi Ana, your order #1 will arrive in 3 days to Seattle. "
        "Confirmation sent to ana@email.com."
    )
