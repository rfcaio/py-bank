from unittest import TestCase

from User import User


class UserTest(TestCase):
    def setUp(self):
        self.user = User('John Doe')

    def test_init(self):
        with self.assertRaises(TypeError):
            User(1)

    def test_name(self):
        self.assertEqual(self.user.name, 'John Doe')

        self.user.name = 'John Connor'
        self.assertEqual(self.user.name, 'John Connor')
