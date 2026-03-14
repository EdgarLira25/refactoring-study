class OrderWorkflowBefore:
    def next_step(
        self,
        is_canceled: bool,
        is_paid: bool,
        has_stock: bool,
        is_address_valid: bool,
    ) -> str:
        result = ""
        if is_canceled:
            result = "stop"
        else:
            if not is_address_valid:
                result = "fix_address"
            else:
                if not has_stock:
                    result = "backorder"
                else:
                    if not is_paid:
                        result = "await_payment"
                    else:
                        result = "ship"
        return result
