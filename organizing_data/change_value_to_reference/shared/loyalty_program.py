from organizing_data.change_value_to_reference.after import OrderAfter
from organizing_data.change_value_to_reference.before import OrderBefore


class LoyaltyProgram:
    def upgrade_if_eligible(self, order: OrderBefore | OrderAfter):
        if order.total >= 1000:
            order.customer.loyalty_tier = "gold"
