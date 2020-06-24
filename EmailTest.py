from unittest import TestCase

from Email import Email

from exceptions import InvalidEmailError


class EmailTest(TestCase):
    def setUp(self):
        self.email = Email('johndoe@pybank.com')

    def test_init(self):
        with self.assertRaises(TypeError):
            Email(0)

        # an email must have at least 6 characters
        with self.assertRaises(InvalidEmailError):
            Email('john@pybank.com')

        # an email must start with an alphabetic character
        with self.assertRaises(InvalidEmailError):
            Email('1johndoe@pybank.com')

        # an email can not have more than 20 characters
        with self.assertRaises(InvalidEmailError):
            Email('abcdefghij_0123456789@pybank.com')

        # an email must finish with pybank.com
        with self.assertRaises(InvalidEmailError):
            Email('johndoe@mail.com')

    def test_value(self):
        with self.assertRaises(AttributeError):
            self.email.value = 'johndoe@mail.org'

        self.assertEqual(self.email.value, 'johndoe@pybank.com')
