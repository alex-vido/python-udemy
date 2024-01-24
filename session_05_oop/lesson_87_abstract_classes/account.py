from abc import ABC, abstractmethod
import re

class Account(ABC):
    def __init__(self, ag, ac, balance):
        self._ag = ag
        self._ac = ac
        self._balance = balance

    @property
    def agency(self):
        return self._ag

    @property
    def account(self):
        return self._ac

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance needs to be numeric')
        self._balance = value

    def deposit(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Deposit value needs to be numeric')
        self._balance += value
        self.information()

    def information(self):
        print(f'Agency: {self._ag}', end=' ')
        print(f'Account: {self._ac}', end=' ')
        print(f'Balance: {self._balance}')

    @abstractmethod
    def withdraw(self, value):
        pass
