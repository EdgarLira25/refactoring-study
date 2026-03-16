class ReservationCalendarBefore:
    def __init__(self, blocked_dates: list[str] | None = None) -> None:
        self.blocked_dates = blocked_dates or []

    def is_available(self, date: str) -> bool:
        return date not in self.blocked_dates


class RoomScheduleBefore(ReservationCalendarBefore):
    def __init__(self, room_name: str, blocked_dates: list[str] | None = None) -> None:
        super().__init__(blocked_dates=blocked_dates)
        self.room_name = room_name

    def book(self, date: str) -> bool:
        if not self.is_available(date):
            return False
        self.blocked_dates.append(date)
        return True
