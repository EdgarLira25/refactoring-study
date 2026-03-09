class OrderServiceBefore:

    def apply_discount(self, order: dict):
        if order["customer"]["type"] == "premium":
            order["total"] *= 0.9
        return order

    def calculate_shipping(self, order: dict) -> float:
        if order["total"] > 500:
            return 0

        if order["customer"]["country"] == "BR":
            return 20

        return 50

    def is_high_value(self, order: dict) -> bool:
        return order["total"] > 1000

    def send_confirmation(self, order: dict):
        email = order["customer"]["email"]
        total = order["total"]
        order_id = order["id"]

        return (
            f"Sending confirmation to {email} for order {order_id} with total {total}"
        )

    def upgrade_loyalty(self, order: dict):
        if order["customer"]["type"] == "regular" and order["total"] > 2000:
            order["customer"]["type"] = "premium"
        return order

    def mark_as_processed(self, order: dict):
        order["status"] = "processed"
        return order
