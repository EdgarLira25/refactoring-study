from encapsulation.remove_middle_man.shared import Department


class EmployeeBefore:
    def __init__(self, name: str, department: Department):
        self.name = name
        self.department = department

    def manager_name(self) -> str:
        return self.department.manager.name

    def manager_email(self) -> str:
        return self.department.manager.email

    def manager_years_in_company(self) -> int:
        return self.department.manager.years_in_company

    def department_budget(self) -> float:
        return self.department.monthly_budget

    def can_request_fast_approval(self, amount: float) -> bool:
        max_fast_approval = self.department_budget() * 0.05
        return amount <= max_fast_approval and self.manager_years_in_company() >= 2


class ExpenseApprovalBefore:
    def __init__(self, employee: EmployeeBefore):
        self.employee = employee

    def approval_summary(self, amount: float) -> str:
        manager = self.employee.manager_name()
        email = self.employee.manager_email()

        if self.employee.can_request_fast_approval(amount):
            return f"Fast approval by {manager} ({email}) " f"for amount ${amount:.2f}"

        return (
            f"Regular flow for amount ${amount:.2f}. "
            f"Manager in charge: {manager} ({email})"
        )
