from unittest import TestCase

from account import Account


class TestAccount(TestCase):
    def test_account_should_initialize_an_account_properly(self):
        id = 477
        owner = 'John Connor'
        balance = 100.0
        limit = 1000.0

        a = Account(id, owner, balance, limit)

        self.assertEqual(a.id, id)
        self.assertEqual(a.owner, owner)
        self.assertEqual(a.balance, balance)
        self.assertEqual(a.limit, limit)
