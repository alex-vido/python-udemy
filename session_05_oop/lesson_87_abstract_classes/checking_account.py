from account import Account

class CheckingAccount(Account):
    def __init__(self, name, age, ag, ac, balance, limit=100):
        super().__init__(name, age, ag, ac, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, value):
        if (self._balance + self._limit) < value:
            print('Insufficient funds')
            return

        self.balance -= value
        self.information()
