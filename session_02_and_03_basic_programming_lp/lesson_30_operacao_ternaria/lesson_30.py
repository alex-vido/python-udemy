"""
Operador ternário
"""
logged_user = True
msg_1 = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
# msg = 'Usuário logado.' if (logged_user == True) else 'Usuário precisa logar.'
print(msg_1)

idade = input('Qual a sua idade: ')

if not idade.isnumeric():
    print('Você precisa digitar apenas números')
else:
    idade = int(idade)
    e_de_maior = idade >= 18
    msg_2 = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'
    print(msg_2)
