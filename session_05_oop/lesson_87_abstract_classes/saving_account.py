from account import Account

class SavingAccount(Account):
    def withdraw(self, value):
        if self._balance < value:
            print('Insufficient funds')
            return

        self.balance -= value
        self.information()
