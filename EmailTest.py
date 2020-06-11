from unittest import TestCase

from Email import Email


class EmailTest(TestCase):
    def setUp(self):
        self.email = Email('johndoe@mail.com')
