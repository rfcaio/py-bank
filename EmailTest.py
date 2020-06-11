from unittest import TestCase

from Email import Email


class EmailTest(TestCase):
    def setUp(self):
        self.email = Email('johndoe@mail.com')

    def test_value(self):
        with self.assertRaises(AttributeError):
            self.email.value = 'johndoe@mail.org'

        self.assertEqual(self.email.value, 'johndoe@mail.com')
