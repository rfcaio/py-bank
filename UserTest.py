import unittest

from User import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User('John Doe')

    def test_name(self):
        self.assertEqual(self.user.name, 'John Doe')

        self.user.name = 'John Connor'
        self.assertEqual(self.user.name, 'John Connor')
