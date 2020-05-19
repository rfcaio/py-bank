from unittest import TestCase

from Account import Account


class AccountTest(TestCase):
    def setUp(self):
        self.account = Account(100)

    def test_balance(self):
        with self.assertRaises(AttributeError):
            self.account.balance = 10000

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

        with self.assertRaises(ValueError):
            self.account.deposit(0)

        self.account.deposit(100)
        self.assertEqual(self.account.balance, 200)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        with self.assertRaises(ValueError):
            self.account.withdraw(500)

        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
