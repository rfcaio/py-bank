import re

from exceptions import InvalidCpfError


class Cpf:
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError(
                'Only strings are accepted to create a CPF.'
            )

        if not re.match(r'^\d{11}$', value):
            raise InvalidCpfError('CPF %s is invalid.' % value)

        self.__value = value

    @property
    def value(self):
        return self.__value
