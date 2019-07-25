
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
