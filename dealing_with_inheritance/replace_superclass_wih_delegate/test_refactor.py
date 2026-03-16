import pytest

from dealing_with_inheritance.replace_superclass_wih_delegate.after import (
    ReservationCalendarAfter,
    RoomScheduleAfter,
)
from dealing_with_inheritance.replace_superclass_wih_delegate.before import (
    ReservationCalendarBefore,
    RoomScheduleBefore,
)


@pytest.mark.parametrize(
    "calendar_factory",
    [
        ReservationCalendarBefore,
        ReservationCalendarAfter,
    ],
)
def test_calendar_availability(calendar_factory):
    calendar = calendar_factory(blocked_dates=["2026-03-20"])

    assert calendar.is_available("2026-03-19") is True
    assert calendar.is_available("2026-03-20") is False


@pytest.mark.parametrize("implementation", ["before", "after"])
@pytest.mark.parametrize(
    "first_booking_expected, second_booking_expected",
    [
        (True, False),
    ],
)
def test_room_schedule_booking(
    implementation: str,
    first_booking_expected: bool,
    second_booking_expected: bool,
):
    if implementation == "before":
        room_schedule = RoomScheduleBefore(room_name="Room A", blocked_dates=[])
    else:
        room_schedule = RoomScheduleAfter(room_name="Room A", blocked_dates=[])

    assert room_schedule.book("2026-03-21") is first_booking_expected
    assert room_schedule.book("2026-03-21") is second_booking_expected
