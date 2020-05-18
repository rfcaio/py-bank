from unittest import TestCase

from Account import Account


class TestAccount(TestCase):
    def setUp(self):
        self.account = Account(477, 'John Connor', 100.0, 1000.0)

    def test_deposit_increase_the_account_balance(self):
        self.account.deposit(150.0)
        self.assertEqual(self.account.balance, 250.0)

    def test_print_balance_print_a_message_with_the_owner_balance(self):
        self.assertEqual(self.account.balance, 100.0)

    def test_transfer_transfer_an_amount_to_another_account(self):
        account = Account(478, 'Sarah Connor', 150.0, 1000.0)
        account.transfer(self.account, 25.0)
        self.assertEqual(account.balance, 125.0)
        self.assertEqual(self.account.balance, 125.0)

    def test_withdraw_decrease_the_account_balance(self):
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)

    def test_withdraw_raise_an_error_when_there_is_not_enough_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1500.0)

    def test_balance_get_the_account_balance(self):
        self.assertEqual(self.account.balance, 100.0)

    def test_limit_get_the_account_limit(self):
        self.assertEqual(self.account.limit, 1000.0)

    def test_limit_set_the_account_limit(self):
        self.account.limit = 1500.0
        self.assertEqual(self.account.limit, 1500.0)

    def test_owner_get_the_account_owner(self):
        self.assertEqual(self.account.owner, 'John Connor')
