from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposity(self, value):
        self.balance += value
        self.information()

    def information(self):
        print(f'Agência: {self.agency} '
              f'account: {self.account} '
              f'balance: {self.balance}')

    @abstractmethod
    def withdraw(self, value):
        pass


class savingAccount(Account):
    def withdraw(self, value):
        if self.balance < value:
            print('balance insuficiente')
            return

        self.balance -= value
        self.information()


class checkingAccount(Account):
    def __init__(self, agency, account, balance, limite=100):
        super().__init__(agency, account, balance)
        self.limite = limite

    def sacar(self, value):
        if (self.balance + self.limit) < value:
            print('balance insuficiente')
            return

        self.balance -= value
        self.information()
