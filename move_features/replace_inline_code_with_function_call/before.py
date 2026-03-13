class PayrollBefore:
    def monthly_report(self, employees: list[dict]) -> list[dict]:
        result = []
        for employee in employees:
            base_salary = employee["salary"]
            tax = base_salary * 0.15
            net_salary = base_salary - tax

            result.append({
                "name": employee["name"],
                "net_salary": round(net_salary, 2),
            })

        return result
