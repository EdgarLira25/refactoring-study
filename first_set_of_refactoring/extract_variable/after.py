class SubscriptionBillingAfter:

    def calculate_monthly_price(self, subscription: dict) -> float:
        users = subscription["users"]
        plan = subscription["plan"]
        projects = subscription["projects"]
        country = subscription["country"]

        price = 0
        price += self.calculate_user_price(users, plan)
        price += self.calculate_project_price(users, projects)
        price *= self.calculate_discount_multiplier(users, projects)
        price *= self.calculate_tax_multiplier(country)

        return price

    def calculate_user_price(self, users: int, plan: str):
        if plan == "pro":
            return users * 15
        return users * 10

    def calculate_project_price(self, users: int, projects: int):
        if users * projects > 50:
            return users * projects * 0.2
        return users * projects * 0.1

    def calculate_discount_multiplier(self, users: int, projects: int):
        if users * projects > 100:
            return 0.9
        return 1

    def calculate_tax_multiplier(self, country: str):
        if country == "BR":
            return 1.12
        return 1.2
