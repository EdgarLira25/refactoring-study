class SubscriptionBillingBefore:

    def calculate_monthly_price(self, subscription: dict) -> float:
        # user price // project price // subscription discount // country tax
        return (
            (
                (
                    subscription["users"] * 15
                    if subscription["plan"] == "pro"
                    else subscription["users"] * 10
                )
                + (
                    subscription["users"] * subscription["projects"] * 0.2
                    if subscription["users"] * subscription["projects"] > 50
                    else subscription["users"] * subscription["projects"] * 0.1
                )
            )
            * (0.9 if subscription["users"] * subscription["projects"] > 100 else 1)
        ) * (1.12 if subscription["country"] == "BR" else 1.2)
