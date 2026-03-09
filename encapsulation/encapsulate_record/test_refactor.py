import pytest
from encapsulation.encapsulate_record.after.after import OrderServiceAfter
from encapsulation.encapsulate_record.before import OrderServiceBefore


def get_order():
    return {
        "id": 1,
        "status": "pending",
        "customer": {
            "name": "Edgar",
            "email": "edgar@email.com",
            "type": "premium",
            "country": "BR",
        },
        "items": [
            {"name": "Laptop", "price": 3000, "quantity": 1},
            {"name": "Mouse", "price": 150, "quantity": 2},
        ],
        "total": 3300,
    }


@pytest.fixture()
def order():
    return get_order()


@pytest.mark.parametrize(
    "order_service",
    [
        OrderServiceBefore(),
        OrderServiceAfter(get_order()),
    ],
)
def test_apply_discount(order_service: OrderServiceBefore | OrderServiceAfter, order):
    if isinstance(order_service, OrderServiceBefore):
        order_service.apply_discount(order)
        total = order["total"]
    elif isinstance(order_service, OrderServiceAfter):
        order_service.apply_discount()
        total = order_service.order.total
    assert total == 2970


@pytest.mark.parametrize(
    "order_service",
    [
        OrderServiceBefore(),
        OrderServiceAfter(get_order()),
    ],
)
def test_calculate_shipping(
    order_service: OrderServiceBefore | OrderServiceAfter, order
):
    if isinstance(order_service, OrderServiceBefore):
        shipping = order_service.calculate_shipping(order)
    elif isinstance(order_service, OrderServiceAfter):
        shipping = order_service.calculate_shipping()

    assert shipping == 0


@pytest.mark.parametrize(
    "order_service",
    [
        OrderServiceBefore(),
        OrderServiceAfter(get_order()),
    ],
)
def test_is_high_value(order_service: OrderServiceBefore | OrderServiceAfter, order):
    if isinstance(order_service, OrderServiceBefore):
        result = order_service.is_high_value(order)
    elif isinstance(order_service, OrderServiceAfter):
        result = order_service.is_high_value()

    assert result is True


@pytest.mark.parametrize(
    "order_service",
    [
        OrderServiceBefore(),
        OrderServiceAfter(get_order()),
    ],
)
def test_send_confirmation(
    order_service: OrderServiceBefore | OrderServiceAfter, order
):
    if isinstance(order_service, OrderServiceBefore):
        result = order_service.send_confirmation(order)
    elif isinstance(order_service, OrderServiceAfter):
        result = order_service.send_confirmation()

    assert result == (
        "Sending confirmation to edgar@email.com for order 1 with total 3300"
    )


@pytest.mark.parametrize(
    "order_service",
    [
        OrderServiceBefore(),
        OrderServiceAfter(get_order()),
    ],
)
def test_upgrade_loyalty(order_service: OrderServiceBefore | OrderServiceAfter, order):
    order["customer"]["type"] = "regular"

    if isinstance(order_service, OrderServiceBefore):
        order_service.upgrade_loyalty(order)
        response = order["customer"]["type"]
    elif isinstance(order_service, OrderServiceAfter):
        order_service.order.customer.update_customer_type("regular")
        order_service.upgrade_loyalty()
        response = order_service.order.customer.type
    assert response == "premium"


@pytest.mark.parametrize(
    "order_service",
    [
        OrderServiceBefore(),
        OrderServiceAfter(get_order()),
    ],
)
def test_mark_as_processed(
    order_service: OrderServiceBefore | OrderServiceAfter, order
):
    if isinstance(order_service, OrderServiceBefore):
        order_service.mark_as_processed(order)
        status = order["status"]
    elif isinstance(order_service, OrderServiceAfter):
        order_service.mark_as_processed()
        status = order_service.order.status
    assert status == "processed"
