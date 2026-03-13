class AddressBefore:
    def __init__(self, street: str, city: str):
        self.street = street
        self.city = city


class CustomerBefore:
    def __init__(self, name: str, address: AddressBefore):
        self.name = name
        self.address = address


class CustomerServiceBefore:
    def __init__(self, customer: CustomerBefore) -> None:
        self.customer = customer

    def move_customer(self, new_city: str):
        self.customer.address.city = new_city
