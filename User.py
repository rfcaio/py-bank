from Cpf import Cpf


class User:
    def __init__(self, cpf, name):
        if not isinstance(name, str):
            raise TypeError('%s is not a valid name.' % name)

        try:
            self.__cpf = Cpf(cpf)
        except Exception:
            raise

        self.__name = name

    @property
    def cpf(self):
        return self.__cpf.format()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
