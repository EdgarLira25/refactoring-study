from encapsulation.hide_delegate.shared import Customer


class OrderAfter:
    def __init__(self, order_id: int, customer: Customer, total: float):
        self.order_id = order_id
        self._customer = customer
        self.total = total

    @property
    def country(self):
        return self._customer.address.country

    @property
    def state(self):
        return self._customer.address.state

    @property
    def city(self):
        return self._customer.address.city

    @property
    def customer_name(self):
        return self._customer.name

    @property
    def email(self):
        return self._customer.email


class ShippingServiceAfter:
    def __init__(self, order: OrderAfter):
        self.order = order

    def shipping_zone(self) -> str:
        country = self.order.country
        state = self.order.state

        if country != "US":
            return "INTL"

        if state in ["CA", "WA", "OR"]:
            return "WEST"

        return "STANDARD"


class NotificationServiceAfter:
    def __init__(self, order: OrderAfter):
        self.order = order

    def delivery_message(self, eta_days: int) -> str:
        customer_name = self.order.customer_name
        city = self.order.city
        email = self.order.email

        return (
            f"Hi {customer_name}, your order #{self.order.order_id} "
            f"will arrive in {eta_days} days to {city}. "
            f"Confirmation sent to {email}."
        )
