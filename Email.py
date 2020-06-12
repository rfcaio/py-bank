class Email:
    def __init__(self, value):
        if not isinstance(value, str):
            raise TypeError('Only strings are accepted to create an email.')

        self.__value = value

    @property
    def value(self):
        return self.__value