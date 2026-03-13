class SalesAnalyzerAfter:
    def metrics(self, orders: list[dict]) -> dict:
        high_value_orders = 0
        for order in orders:
            high_value_orders += order["price"] * order["quantity"] >= 1000

        active_customers = {
            order["customer_id"] for order in orders if order["status"] == "paid"
        }

        total_revenue = sum([order["price"] * order["quantity"] for order in orders])

        return {
            "total_revenue": round(total_revenue, 2),
            "high_value_orders": high_value_orders,
            "active_customers": len(active_customers),
        }
