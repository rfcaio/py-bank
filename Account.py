class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('%.2f is not a valid value to deposit.')
        self.__balance += amount

    def transfer(self, amount, destination):
        if not isinstance(destination, Account):
            raise TypeError('Could not transfer to an invalid account.')
        if amount <= 0:
            raise ValueError('%.2f is not a valid value to deposit.')
        try:
            self.withdraw(amount)
        except Exception:
            raise
        destination.deposit(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('%.2f is not a valid value to withdraw.')
        if not self.__have_enough_balance(amount):
            raise ValueError('Not enough balance.')
        self.__balance -= amount

    def __have_enough_balance(self, amount):
        return self.__balance >= amount
