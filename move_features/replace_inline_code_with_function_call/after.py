class PayrollAfter:
    def monthly_report(self, employees: list[dict]) -> list[dict]:
        return [
            {
                "name": employee["name"],
                "net_salary": round(employee["salary"] - employee["salary"] * 0.15, 2),
            }
            for employee in employees
        ]
