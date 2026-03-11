from dataclasses import dataclass


@dataclass
class Address:
    street: str
    city: str
    state: str
    postal_code: str
    country: str

    def update(
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
