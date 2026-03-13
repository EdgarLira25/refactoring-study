from organizing_data.change_value_to_reference.shared.customer import CustomerValue


class DictRepository:
    def __init__(self) -> None:
        self._customers = {}

    def register_customer(self, customer: CustomerValue) -> CustomerValue:
        if customer.customer_id not in self._customers:
            self._customers[customer.customer_id] = customer
        return self.get_customer(customer.customer_id)

    def get_customer(self, customer_id: int) -> CustomerValue:
        return self._customers[customer_id]


repository = DictRepository()


class OrderAfter:
    def __init__(self, order_id: int, customer: CustomerValue, total: float):
        self.order_id = order_id
        self.customer = repository.register_customer(customer)
        self.total = total
