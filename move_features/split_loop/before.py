class SalesAnalyzerBefore:
    def metrics(self, orders: list[dict]) -> dict:
        total_revenue = 0.0
        high_value_orders = 0
        active_customers = set()

        for order in orders:
            value = order["price"] * order["quantity"]
            total_revenue += value

            if value >= 1000:
                high_value_orders += 1

            if order["status"] == "paid":
                active_customers.add(order["customer_id"])

        return {
            "total_revenue": round(total_revenue, 2),
            "high_value_orders": high_value_orders,
            "active_customers": len(active_customers),
        }
