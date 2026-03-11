from datetime import date


class CustomerProfileBefore:
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

        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

        self.subscription_plan = subscription_plan
        self.monthly_fee = monthly_fee
        self.last_payment_date = last_payment_date

    def contact_card(self) -> str:
        return f"{self.name} | {self.email} | {self.phone}"

    def shipping_label(self) -> str:
        return (
            f"{self.name}\n"
            f"{self.street}\n"
            f"{self.city} - {self.state}, {self.postal_code}\n"
            f"{self.country}"
        )

    def update_address(
        self,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
    ):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def monthly_charge_preview(self) -> float:
        tax_rate = 0.07 if self.country == "US" else 0.12
        return self.monthly_fee + (self.monthly_fee * tax_rate)

    def is_payment_overdue(self, today: date) -> bool:
        last_payment = date.fromisoformat(self.last_payment_date)
        days_since_payment = (today - last_payment).days
        return days_since_payment > 30

    def mark_payment_received(self, payment_date: date):
        self.last_payment_date = payment_date.isoformat()
