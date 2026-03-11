from dataclasses import dataclass
from datetime import date


@dataclass
class Subscription:
    subscription_plan: str
    monthly_fee: float
    last_payment_date: str

    def monthly_charge_preview(self, country: str):
        tax_rate = 0.07 if country == "US" else 0.12
        return self.monthly_fee + (self.monthly_fee * tax_rate)

    def is_payment_overdue(self, today: date):
        last_payment = date.fromisoformat(self.last_payment_date)
        days_since_payment = (today - last_payment).days
        return days_since_payment > 30

    def mark_payment_received(self, payment_date: date):
        self.last_payment_date = payment_date.isoformat()
