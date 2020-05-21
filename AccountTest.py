from unittest import TestCase

from Account import Account


class AccountTest(TestCase):
    def setUp(self):
        self.account = Account(100)

    def test_init(self):
        with self.assertRaises(ValueError):
            Account(-100)

        account = Account()
        self.assertEqual(account.balance, 0)

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

    def test_transfer(self):
        destination = Account(50)

        with self.assertRaises(TypeError):
            self.account.transfer(50, {'balance': 50})

        with self.assertRaises(ValueError):
            self.account.transfer(-50, destination)

        with self.assertRaises(ValueError):
            self.account.transfer(0, destination)

        # when trying to transfer an amount greater than the balance
        with self.assertRaises(ValueError):
            self.account.transfer(150, destination)
            self.assertEqual(destination.balance, 50)

        self.account.transfer(50, destination)
        self.assertEqual(self.account.balance, 50)
        self.assertEqual(destination.balance, 100)

    def test_withdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

        with self.assertRaises(ValueError):
            self.account.withdraw(0)

        with self.assertRaises(ValueError):
            self.account.withdraw(500)

        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50)
