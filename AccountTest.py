from unittest import TestCase

from Account import Account


class AccountTest(TestCase):
    def setUp(self):
        self.account = Account(100.0)

    def test_init(self):
        with self.assertRaises(ValueError):
            Account(-100.0)

        account = Account()
        self.assertEqual(account.balance, 0.0)

    def test_balance(self):
        with self.assertRaises(AttributeError):
            self.account.balance = 10000.0

    def test_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

        with self.assertRaises(ValueError):
            self.account.deposit(0.0)

        self.account.deposit(100.0)
        self.assertEqual(self.account.balance, 200.0)

    def test_transfer(self):
        destination = Account(50.0)

        with self.assertRaises(TypeError):
            self.account.transfer(50.0, {'balance': 50.0})

        with self.assertRaises(ValueError):
            self.account.transfer(-50.0, destination)

        with self.assertRaises(ValueError):
            self.account.transfer(0.0, destination)

        # when trying to transfer an amount greater than the balance
        with self.assertRaises(ValueError):
            self.account.transfer(150.0, destination)
            self.assertEqual(destination.balance, 50.0)

        self.account.transfer(50.0, destination)
        self.assertEqual(self.account.balance, 50.0)
        self.assertEqual(destination.balance, 100.0)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100.0)

        with self.assertRaises(ValueError):
            self.account.withdraw(0.0)

        with self.assertRaises(ValueError):
            self.account.withdraw(500.0)

        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)
