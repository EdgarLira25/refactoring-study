class Address:
    def __init__(self, street: str, city: str, state: str, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.country = country


class Customer:
    def __init__(self, name: str, email: str, address: Address):
        self.name = name
        self.email = email
        self.address = address
