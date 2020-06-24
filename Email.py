import re

from exceptions import InvalidEmailError


class Email:
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError('Only strings are accepted to create an email.')

        if not self.__is_valid_email(value):
            raise InvalidEmailError('Email %s is invalid.' % value)

        self.__value = value

    def __is_valid_email(self, value):
        EMAIL_REGEX = r'^[a-z][0-9a-z_]{5,19}@pybank\.com$'
        return re.match(EMAIL_REGEX, value)

    @property
    def value(self):
        return self.__value
