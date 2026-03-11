from encapsulation.hide_delegate.shared import Customer


class OrderBefore:
    def __init__(self, order_id: int, customer: Customer, total: float):
        self.order_id = order_id
        self.customer = customer
        self.total = total


class ShippingServiceBefore:
    def __init__(self, order: OrderBefore):
        self.order = order

    def shipping_zone(self) -> str:
        country = self.order.customer.address.country
        state = self.order.customer.address.state

        if country != "US":
            return "INTL"

        if state in ["CA", "WA", "OR"]:
            return "WEST"

        return "STANDARD"


class NotificationServiceBefore:
    def __init__(self, order: OrderBefore):
        self.order = order

    def delivery_message(self, eta_days: int) -> str:
        customer_name = self.order.customer.name
        city = self.order.customer.address.city
        email = self.order.customer.email

        return (
            f"Hi {customer_name}, your order #{self.order.order_id} "
            f"will arrive in {eta_days} days to {city}. "
            f"Confirmation sent to {email}."
        )
