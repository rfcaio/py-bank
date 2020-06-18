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

    def __generate_cpf(self, incomplete_cpf):
        if len(incomplete_cpf) == 11:
            return incomplete_cpf

        return self.__generate_cpf(
            incomplete_cpf + self.__get_verify_digit(incomplete_cpf)
        )

    def __get_verify_digit(self, incomplete_cpf):
        multiplier = len(incomplete_cpf) + 1
        digit_sum = 0
        for digit in incomplete_cpf:
            digit_sum += int(digit) * multiplier
            multiplier -= 1
        factor = digit_sum % 11
        return str(11 - factor if factor >= 2 else 0)

    def __is_valid_cpf(self, cpf):
        EQUAL_DIGITS_CPFS = [str(i) * 11 for i in range(0, 10)]

        if cpf in EQUAL_DIGITS_CPFS:
            return False

        first_nine_cpf_digits = cpf[0:9]

        return cpf == self.__generate_cpf(first_nine_cpf_digits)
