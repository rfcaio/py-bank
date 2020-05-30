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
            Cpf('1844269906')

        with self.assertRaises(InvalidCpfError):
            Cpf('184426990600')

        with self.assertRaises(InvalidCpfError):
            Cpf('abcdefghijk')

        with self.assertRaises(InvalidCpfError):
            Cpf('00000000000')

        with self.assertRaises(InvalidCpfError):
            Cpf('18442699067')

    def test_format(self):
        self.assertEqual(self.cpf.format(), '184.426.990-66')

    def test_value(self):
        with self.assertRaises(AttributeError):
            self.cpf.value = '63204728048'
