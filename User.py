class User:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError('%s is not a valid name.' % name)

        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name
