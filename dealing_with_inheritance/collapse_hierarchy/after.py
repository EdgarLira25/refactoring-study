class NotificationAfter:
    def __init__(self, message: str) -> None:
        self.message = message

    def send(self) -> str:
        return f"Notify: {self.message}"
