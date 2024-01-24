from saving_account import SavingAccount
from checking_account import CheckingAccount

sa = SavingAccount(1111, 2222, 0)
sa.deposit(10)
sa.withdraw(5)
sa.withdraw(10)
sa.information()
sa.withdraw(5)

print('\n', '#' * 50, '\n')

ca = CheckingAccount(ag=1111, ac=2222, balance=0, limit=500)
ca.withdraw(400)
ca.withdraw(50)
ca.withdraw(1)
ca.deposit(150)
