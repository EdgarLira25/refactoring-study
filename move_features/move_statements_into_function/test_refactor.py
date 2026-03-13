import pytest

from move_features.move_statements_into_function.after import OrderNotifierAfter
from move_features.move_statements_into_function.before import OrderNotifierBefore


def list_notifiers():
    name = " edgar lira "
    email = " Teste@Email.com "
    return [
        OrderNotifierBefore(customer_name=name, customer_email=email),
        OrderNotifierAfter(customer_name=name, customer_email=email),
    ]


@pytest.mark.parametrize("notifier", list_notifiers())
def test_send_paid_notification(notifier: OrderNotifierBefore | OrderNotifierAfter):
    assert notifier.send_paid_notification(order_id=101, total=250.5) == {
        "to": "teste@email.com",
        "subject": "Order #101 payment confirmed",
        "body": "Hi Edgar Lira, we received your payment of $250.50.",
    }


@pytest.mark.parametrize("notifier", list_notifiers())
def test_normalization_and_greeting(notifier: OrderNotifierBefore | OrderNotifierAfter):
    result = notifier.send_paid_notification(order_id=1, total=10.0)
    assert result["to"] == "teste@email.com"
    assert result["body"].startswith("Hi Edgar Lira, we received your payment of $10.00.")


@pytest.mark.parametrize("notifier", list_notifiers())
def test_send_shipped_notification(notifier: OrderNotifierBefore | OrderNotifierAfter):
    assert notifier.send_shipped_notification(order_id=101, tracking_code="BR123") == {
        "to": "teste@email.com",
        "subject": "Order #101 shipped",
        "body": "Hi Edgar Lira, your tracking code is BR123.",
    }
