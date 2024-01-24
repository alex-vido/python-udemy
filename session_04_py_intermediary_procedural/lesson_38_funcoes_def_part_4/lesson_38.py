"""
Escopo global - Escopo local
"""

variavel = 'valor'


def func():
    print(variavel)


"""
def func_2():
    global variavel  # Não é uma boa prática de programação
    variavel = 'outro valor'
    print(variavel)
"""


def func_2(arg=None):
    arg = arg.replace('v', 'b')
    return arg


func()
outra_variavel = func_2(arg=variavel)
print(outra_variavel)
