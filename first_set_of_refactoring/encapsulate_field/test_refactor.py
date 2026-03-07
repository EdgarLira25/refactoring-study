import pytest
from first_set_of_refactoring.encapsulate_field.after import BankAccountAfter
from first_set_of_refactoring.encapsulate_field.before import BankAccountBefore


@pytest.mark.parametrize(
    "initial_balance, deposit, withdraw, expected",
    [
        (100, 50, 20, 120),
        (200, 100, 50, 240),
    ],
)
@pytest.mark.parametrize("account_class", [BankAccountBefore, BankAccountAfter])
def test_bank_account(account_class, initial_balance, deposit, withdraw, expected):
    account = account_class(initial_balance)

    account.deposit(deposit)
    account.withdraw(withdraw)
    account.apply_monthly_fee()

    assert account.balance == expected
