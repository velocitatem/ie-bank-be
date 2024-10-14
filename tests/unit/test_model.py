from iebank_api.models import Account
from iebank_api.routes import format_account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'ESP')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'


def test_country_field():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the country field is defined correctly
    """
    account = Account('John Doe', '€', 'ESP')
    assert account.country == 'ESP'

def test_account_repr():
    """
    GIVEN a Account model
    WHEN the model is printed
    THEN check the representation is valid
    """
    account = Account('John Doe', '€', 'ESP')
    assert repr(account) == '<Event %r>' % account.account_number
    formated = format_account(account)
    assert formated['name'] == account.name
    assert formated['currency'] == account.currency
    assert formated['account_number'] == account.account_number
    assert formated['balance'] == account.balance
    assert formated['status'] == account.status
    assert formated['created_at'] == account.created_at
    assert formated['country'] == account.country
    assert formated['id'] == account.id
