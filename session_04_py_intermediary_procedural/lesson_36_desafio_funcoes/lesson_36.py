"""
1- Crie uma função que exiba saudação com os parametros saudação e nome

2 - Crie uma função que receba 3 números e exiba a soma entre eles

3 - Crie uma função que receba 2 números. O primeiro é um valor e o 2 é porcentagem (ex:10%).
Retorne o 1 valor somado ao aumento percentual do mesmo.

4 - Fizz Buzz. Se o parametro for divisivel por 2 retorne Fizz, se for divisivel por 5:
retorne Buzz. Se for divisivel por 2 e por 5 retorne Fizz Buzz.
"""

# 1:
from calendar import different_locale
from string import octdigits
from turtle import left


def saudacao(saudacao, nome):
    return saudacao, nome

print(saudacao('Olá', 'Alex'))

# 2:
def soma(n1, n2, n3):
    return n1 + n2 + n3

print(soma(5, 4, 3))

# 3:
def aumento_percentual(numero, percentual):
    # percentual = porcentagem / 100
    # aumento = percentual * numero
    # return numero + aumento
    return numero + (numero * percentual / 100)

print(aumento_percentual(100, 80))

def fizzbuzz(n):
    if n % 15 == 0:
        return 'Fizz Buzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return f'{n} não é divisivel nem por 5 nem por 2'

print(fizzbuzz(5))
