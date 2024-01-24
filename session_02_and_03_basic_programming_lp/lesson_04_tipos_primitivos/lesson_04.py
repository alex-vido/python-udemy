"""
Tipos primitivos

str  String - Textos "Assim" ou 'assim'
int inteiro - 1 10 50 -100 -500 523
float - 10.50 1.5 -10.10
bool boolean - True/False 10 == 10
"""
print("Alex", type("Alex"))
print("10", type("10"))
print(10, type(10))
print(10.5, type(10.5))
print(10 == 10, type(10 == 10))
print(bool(''))  # False
print("Luiz", type("Luiz"), bool("Luiz"))
print("10", type('10'), type(int(10)))

#  Exercicio

#  nome
print("Alex", type("Alex"))
#  idade
print(29, type(29))
#  altura
print(1.64, type(1.64))
#  maior de idade
print(29 > 18, type(29 > 18))
