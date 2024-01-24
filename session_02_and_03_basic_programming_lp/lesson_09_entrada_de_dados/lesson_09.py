"""

Entrada de dados
* Input sempre retorna uma str

"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
ano_nascimento = 2022 - int(idade)
print(f'O seu nome é {nome} e tem {idade} anos.')
print(f'{nome} nasceu em {ano_nascimento}')

# converter de um tipo de valor para outro se chama Type Cast
numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite outro número: ')
numero_2 = int(numero_2)
soma = numero_1 + numero_2
print(f'{numero_1} + {numero_2} = {soma}')
