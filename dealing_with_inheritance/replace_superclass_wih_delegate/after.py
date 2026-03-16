class RoomScheduleAfter:
    def __init__(self, room_name: str, blocked_dates: list[str] | None = None) -> None:
        self.room_name = room_name
        self.calendar = ReservationCalendarAfter(blocked_dates=blocked_dates)

    def is_available(self, date: str) -> bool:
        return self.calendar.is_available(date)

    def book(self, date: str) -> bool:
        return self.calendar.book(date)


class ReservationCalendarAfter:
    def __init__(self, blocked_dates: list[str] | None = None) -> None:
        self.blocked_dates = blocked_dates or []

    def is_available(self, date: str) -> bool:
        return date not in self.blocked_dates

    def book(self, date: str) -> bool:
        if not self.is_available(date):
            return False
        self.blocked_dates.append(date)
        return True
