from encapsulation.encapsulate_record.after.models import Order


class OrderServiceAfter:
    def __init__(self, order: dict) -> None:
        self.order = Order.from_dict(order)

    def apply_discount(self):
        if self.order.customer.type == "premium":
            self.order.apply_discount(0.9)

    def calculate_shipping(self) -> float:
        if self.order.total > 500:
            return 0
        if self.order.customer.country == "BR":
            return 20
        return 50

    def is_high_value(self) -> bool:
        return self.order.total > 1000

    def send_confirmation(self):
        return f"Sending confirmation to {self.order.customer.email} for order {self.order.id} with total {self.order.total}"

    def upgrade_loyalty(self):
        if self.order.customer.type == "regular" and self.order.total > 2000:
            self.order.customer.update_customer_type("premium")

    def mark_as_processed(self):
        self.order.update_order_status("processed")
