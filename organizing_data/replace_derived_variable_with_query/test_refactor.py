import pytest

from organizing_data.replace_derived_variable_with_query.after import AccountAfter
from organizing_data.replace_derived_variable_with_query.before import AccountBefore


def list_accounts():
    return [AccountBefore(owner="Teste"), AccountAfter(owner="Teste")]


@pytest.mark.parametrize("account", list_accounts())
def test_add_and_remove_transactions(account: AccountBefore | AccountAfter):
    account.add_transaction(1000.0)
    account.add_transaction(-200.0)
    account.remove_transaction(-200.0)

    assert account.balance == 1000.0


@pytest.mark.parametrize("account", list_accounts())
def test_apply_monthly_fee(account: AccountBefore | AccountAfter):
    account.add_transaction(500.0)
    account.apply_monthly_fee(50.0)

    assert account.balance == 450.0


@pytest.mark.parametrize("account", list_accounts())
def test_summary(account: AccountBefore | AccountAfter):
    account.add_transaction(250.0)

    assert account.summary() == "Teste balance: $250.00"
