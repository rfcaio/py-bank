import re

from exceptions import InvalidCpfError


class Cpf:
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError(
                'Only strings are accepted to create a CPF.'
            )

        if not (re.match(r'^\d{11}$', value) and self.__is_valid_cpf(value)):
            raise InvalidCpfError('CPF %s is invalid.' % value)

        self.__value = value

    def format(self):
        cpf_parts = re.match(r'^(\d{3})(\d{3})(\d{3})(\d{2})$', self.__value)
        return cpf_parts.expand(r'\g<1>.\g<2>.\g<3>-\g<4>')

    @property
    def value(self):
        return self.__value

    def __get_verify_digit(self, cpf):
        multiplier = len(cpf) + 1
        digit_sum = 0
        for digit in cpf:
            digit_sum += int(digit) * multiplier
            multiplier -= 1
        factor = digit_sum % 11
        return str(11 - factor if factor >= 2 else 0)

    def __is_valid_cpf(self, cpf):
        EQUAL_DIGITS_CPFS = [str(i) * 11 for i in range(0, 10)]

        if cpf in EQUAL_DIGITS_CPFS:
            return False

        first_nine_digits = cpf[0:9]
        first_check_digit = self.__get_verify_digit(first_nine_digits)
        second_check_digit = (
            self.__get_verify_digit(first_nine_digits + first_check_digit)
        )
        obtained_cpf = (
            first_nine_digits + first_check_digit + second_check_digit
        )
        return cpf == obtained_cpf
