from unittest import TestCase

from Cpf import Cpf

from exceptions import InvalidCpfError


class CpfTest(TestCase):
    def setUp(self):
        self.cpf = Cpf('18442699066')

    def test_init(self):
        with self.assertRaises(TypeError):
            Cpf(18442699066)

        with self.assertRaises(InvalidCpfError):
            Cpf('1844269906a')

        with self.assertRaises(InvalidCpfError):
            Cpf('184426990600')

        with self.assertRaises(InvalidCpfError):
            Cpf('1844269906')

    def test_value(self):
        with self.assertRaises(AttributeError):
            self.cpf.value = '63204728048'
