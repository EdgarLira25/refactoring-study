import pytest

from dealing_with_inheritance.replace_subclass_with_delegate.after import (
    BookingAfter,
    PremiumSupportDelegateAfter,
)
from dealing_with_inheritance.replace_subclass_with_delegate.before import (
    BookingBefore,
    PremiumBookingBefore,
)


@pytest.mark.parametrize("implementation", ["before", "after"])
@pytest.mark.parametrize(
    "is_premium, expected_priority, expected_summary",
    [
        (False, False, "Ana booking"),
        (True, True, "Ana booking with priority support"),
    ],
)
def test_booking_priority_behavior(
    implementation: str,
    is_premium: bool,
    expected_priority: bool,
    expected_summary: str,
):
    if implementation == "before":
        if is_premium:
            booking = PremiumBookingBefore(customer_name="Ana")
        else:
            booking = BookingBefore(customer_name="Ana")
    else:
        if is_premium:
            booking = BookingAfter(
                customer_name="Ana",
                premium_support_delegate=PremiumSupportDelegateAfter(),
            )
        else:
            booking = BookingAfter(customer_name="Ana")

    assert booking.has_priority_support() is expected_priority
    assert booking.summary() == expected_summary
