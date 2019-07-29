
class Account:
    def __init__(self, id, owner, balance, limit):
        self.__id = id
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit


    def deposit(self, amount):
        self.__balance += amount


    def print_balance(self):
        return 'Your account balance is $ {}.'.format(self.__balance)


    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)


    def withdraw(self, amount):
        self.__balance -= amount


    @property
    def balance(self):
        return self.__balance


    @property
    def limit(self):
        return self.__limit


    @limit.setter
    def limit(self, limit):
        self.__limit = limit


    @property
    def owner(self):
        return self.__owner
