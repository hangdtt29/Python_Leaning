# test_wallet.py

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.mark.ini
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

@pytest.mark.ini
def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

# @pytest.fixture
# def empty_wallet():
#     '''Returns a Wallet instance with a zero balance'''
#     return Wallet()

# @pytest.fixture
# def wallet():
#     '''Returns a Wallet instance with a balance of 20'''
#     return Wallet(20)

# @pytest.mark.parametrize("earned,spent,expected", [
#     (30, 10, 20),
#     (20, 2, 18),
# ])
# def test_transactions(earned, spent, expected):
#     my_wallet = Wallet()
#     my_wallet.add_cash(earned)
#     my_wallet.spend_cash(spent)
#     assert my_wallet.balance == expected

# Kết hợp fixture và parametrize
# @pytest.fixture
# def my_wallet():
#     '''Returns a Wallet instance with a zero balance'''
#     return Wallet()

# @pytest.mark.parametrize("earned,spent,expected", [
#     (30, 10, 20),
#     (20, 2, 18),
# ])
# def test_transactions(my_wallet, earned, spent, expected):
#     my_wallet.add_cash(earned)
#     my_wallet.spend_cash(spent)
#     assert my_wallet.balance == expected