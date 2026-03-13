class OrderNotifierAfter:
    def __init__(self, customer_name: str, customer_email: str):
        self.customer_name = customer_name
        self.customer_email = customer_email

    def send_paid_notification(self, order_id: int, total: float) -> dict:
        greeting = f"Hi {self.customer_name.strip().title()}"
        subject = f"Order #{order_id} payment confirmed"
        body = f"{greeting}, we received your payment of ${total:.2f}."

        return self._build_email(subject, body)

    def send_shipped_notification(self, order_id: int, tracking_code: str) -> dict:
        greeting = f"Hi {self.customer_name.strip().title()}"
        subject = f"Order #{order_id} shipped"
        body = f"{greeting}, your tracking code is {tracking_code}."

        return self._build_email(subject, body)

    def _build_email(self, subject: str, body: str) -> dict:
        return {
            "to": self.customer_email.strip().lower(),
            "subject": subject,
            "body": body,
        }
