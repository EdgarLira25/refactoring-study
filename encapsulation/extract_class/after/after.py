from datetime import date

from encapsulation.extract_class.after.address import Address
from encapsulation.extract_class.after.subscription import Subscription


class CustomerProfileAfter:
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        subscription_plan: str,
        monthly_fee: float,
        last_payment_date: str,
    ):
        self.name = name
        self.email = email
        self.phone = phone

        self.address = Address(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )
        self.subscription = Subscription(
            subscription_plan=subscription_plan,
            monthly_fee=monthly_fee,
            last_payment_date=last_payment_date,
        )

    def contact_card(self) -> str:
        return f"{self.name} | {self.email} | {self.phone}"

    def shipping_label(self) -> str:
        return (
            f"{self.name}\n"
            f"{self.address.street}\n"
            f"{self.address.city} - {self.address.state}, {self.address.postal_code}\n"
            f"{self.address.country}"
        )

    def update_address(
        self,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
    ):
        self.address.update(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )

    def monthly_charge_preview(self) -> float:
        return self.subscription.monthly_charge_preview(self.address.country)

    def is_payment_overdue(self, today: date) -> bool:
        return self.subscription.is_payment_overdue(today)

    def mark_payment_received(self, payment_date: date):
        self.subscription.mark_payment_received(payment_date)
