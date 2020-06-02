from unittest import TestCase

from User import User

from exceptions import InvalidCpfError


class UserTest(TestCase):
    def setUp(self):
        self.user = User('63204728048', 'John Doe')

    def test_init(self):
        with self.assertRaises(InvalidCpfError):
            User('63204728049', 'John Doe')

        with self.assertRaises(TypeError):
            User('63204728048', 1)

    def test_cpf(self):
        with self.assertRaises(AttributeError):
            self.user.cpf = '18442699066'

        self.assertEqual(self.user.cpf, '632.047.280-48')

    def test_name(self):
        self.assertEqual(self.user.name, 'John Doe')

        self.user.name = 'John Connor'
        self.assertEqual(self.user.name, 'John Connor')
