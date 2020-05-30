from exceptions import InsufficientBalanceError


class Account:
    def __init__(self, balance=0):
        if not (isinstance(balance, float) or isinstance(balance, int)):
            raise TypeError('Only numbers are accepted to create an account.')

        if balance < 0:
            raise ValueError('%.2f is not a valid account balance.' % balance)

        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('%.2f is not a valid value to deposit.' % amount)

        self.__balance += amount

    def transfer(self, amount, destination):
        if not isinstance(destination, Account):
            raise TypeError('Could not transfer to an invalid account.')

        if amount <= 0:
            raise ValueError('%.2f is not a valid value to deposit.' % amount)

        try:
            self.withdraw(amount)
        except Exception:
            raise
        destination.deposit(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('%.2f is not a valid value to withdraw.' % amount)

        if not self.__have_enough_balance(amount):
            raise InsufficientBalanceError('Not enough balance.')

        self.__balance -= amount

    def __have_enough_balance(self, amount):
        return self.__balance >= amount
