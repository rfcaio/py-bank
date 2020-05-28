from unittest import TestCase

from Cpf import Cpf


class CpfTest(TestCase):
    def setUp(self):
        self.cpf = Cpf('18442699066')

    def test_init(self):
        with self.assertRaises(TypeError):
            Cpf(18442699066)

    def test_value(self):
        with self.assertRaises(AttributeError):
            self.cpf.value = '63204728048'
