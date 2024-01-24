# https://docs.python.org/3/library/exceptions.html

'''
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log: ', error)
        raise  # Erro será logado em algum arquivo de erro

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)  # Possível erro mostrado posteriormente
'''


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero')
    return n1 / n2

try:
    print(divide(2, 0))
except ValueError as error:
    print('Você está tentando dividir por 0.')
