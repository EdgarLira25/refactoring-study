class OrderWorkflowAfter:
    def next_step(
        self,
        is_canceled: bool,
        is_paid: bool,
        has_stock: bool,
        is_address_valid: bool,
    ) -> str:
        if is_canceled:
            return "stop"
        if not is_address_valid:
            return "fix_address"
        if not has_stock:
            return "backorder"
        if not is_paid:
            return "await_payment"
        return "ship"
