from dataclasses import dataclass, replace


@dataclass(frozen=True)
class AddressAfter:
    street: str
    city: str

    def with_city(self, city: str):
        return replace(self, city=city)


class CustomerAfter:
    def __init__(self, name: str, address: AddressAfter):
        self.name = name
        self.address = address

    def update_address_city(self, city: str):
        self.address = self.address.with_city(city)


class CustomerServiceAfter:
    def __init__(self, customer: CustomerAfter) -> None:
        self.customer = customer

    def move_customer(self, new_city: str):
        self.customer.update_address_city(new_city)
