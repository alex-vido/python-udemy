'''
1 - Crie uma funcao1 que receba outra funcao2 como parametro e retorne o valor da funcao2 executada
'''


def ola_mundo():
    return 'olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)

"""
2 - Crie uma funcao1 que receba outra funcao2 como parametro e retorne o valor da funcao2 executada.
Faça a funcao1 executar 2 funcoes que recebam um numero diferente de argumentos
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando1 = mestre(fala_oi, 'Alex')
executando2 = mestre(saudacao, 'Alex', saudacao='Boa noite')
print(executando1)
print(executando2)
