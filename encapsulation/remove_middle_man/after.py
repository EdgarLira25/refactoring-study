from encapsulation.remove_middle_man.shared import Department


class EmployeeAfter:
    def __init__(self, name: str, department: Department):
        self.name = name
        self.department = department

    def can_request_fast_approval(self, amount: float) -> bool:
        return (
            amount <= self.department.monthly_budget * 0.05
            and self.department.manager.years_in_company >= 2
        )


class ExpenseApprovalAfter:
    def __init__(self, employee: EmployeeAfter):
        self.employee = employee

    def approval_summary(self, amount: float) -> str:
        manager = self.employee.department.manager.name
        email = self.employee.department.manager.email

        if self.employee.can_request_fast_approval(amount):
            return f"Fast approval by {manager} ({email}) " f"for amount ${amount:.2f}"

        return (
            f"Regular flow for amount ${amount:.2f}. "
            f"Manager in charge: {manager} ({email})"
        )
