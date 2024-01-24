"""
Funções - def
"""
"""
def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)  # Não é costume usar print em funções

saudacao()
saudacao(msg='Oi', nome='Pedro')
saudacao('Alex')
saudacao(nome='Yuri', msg='Hello')
"""
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

dividir = divisao(8, 4)

if dividir:
    print(dividir)
else:
    print('Conta inválida.')

print('##############################################################')

def f(var):
    print(var)

def dumb():
    return f

var = dumb()('Mensagem do f, sendo executada pelo dumb')
