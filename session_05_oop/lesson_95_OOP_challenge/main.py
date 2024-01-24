"""
Exercise with abstraction, inheritance, encapsulation and polymorphism
Create a bank system (simply) it have clients, accounts and a bank. Saving account and
checking account and can deposity/withdraw money.

Hints:
Create a class Client it inheritance of Person class
    Person have name and age(with getters)
    Client have account(Class aggregation saving or checking account)
Create classes CheckingAccount and SavingAccount it inheritance from Account
    CheckingAccount must have a extra limit
    Accounts have branch, account number and balance
    Account must have deposity method
    Account (superclass) need to have withdraw abstract method (inheritance and polymorphism
    - Subclass implement the withdraw method)
Create a bank for aggregation clients and accounts classes
Bank will be responsable for autheticate clients and accounts:
    Bank have accounts and clients
    * Check if the account is from that bank
    * Check if the client if from that bank
    * Check if the agency is from that bank
Only after this authentication the client will be able to withdraw.

"""
from bank import Bank
from client import Client
from account import savingAccount, checkingAccount

bank = Bank()

client_1 = Client('Luiz', 30)
client_2 = Client('Maria', 18)
client_3 = Client('João', 50)

ac1 = savingAccount(1111, 254136, 0)
ac2 = savingAccount(2222, 254137, 0)
ac3 = savingAccount(1212, 254138, 0)

client_1.insert_account(ac1)
client_2.insert_account(ac2)
client_3.insert_account(ac3)

bank.insert_client(client_1)
bank.insert_account(ac1)

bank.insert_client(client_2)
bank.insert_account(ac2)

if bank.authenticate(client_1):
    client_1.account.deposity(0)
    client_1.account.withdraw(20)
else:
    print('Cliente não autenticado.')

print('####################')

if bank.authenticate(client_2):
    client_2.account.deposity(0)
    client_2.account.withdraw(20)
else:
    print('Cliente não autenticado.')
