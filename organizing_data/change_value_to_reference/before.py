from organizing_data.change_value_to_reference.shared.customer import CustomerValue


class OrderBefore:
    def __init__(self, order_id: int, customer: CustomerValue, total: float):
        self.order_id = order_id
        self.customer = customer
        self.total = total
