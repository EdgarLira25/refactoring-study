import pytest

from refactoring_apis.remove_flag_argument.after import BookingServiceAfter
from refactoring_apis.remove_flag_argument.before import BookingServiceBefore


def list_booking_services():
    return [BookingServiceBefore(), BookingServiceAfter()]


@pytest.mark.parametrize("service", list_booking_services())
def test_premium_booking_path(
    service: BookingServiceBefore | BookingServiceAfter,
):
    if isinstance(service, BookingServiceBefore):
        message = service.booking_message("Ana", True)
        days = service.delivery_days(True)
    else:
        message = service.booking_message_premium("Ana")
        days = service.delivery_days_premium()

    assert message == "Priority booking confirmed for Ana"
    assert days == 1


@pytest.mark.parametrize("service", list_booking_services())
def test_regular_booking_path(
    service: BookingServiceBefore | BookingServiceAfter,
):
    if isinstance(service, BookingServiceBefore):
        message = service.booking_message("Ana", False)
        days = service.delivery_days(False)
    else:
        message = service.booking_message_regular("Ana")
        days = service.delivery_days_regular()

    assert message == "Standard booking confirmed for Ana"
    assert days == 5
