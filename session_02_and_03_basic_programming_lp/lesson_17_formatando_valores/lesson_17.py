"""

Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante
:. (Número)f - Quantidade de casas decimais (float)
: (caractere) (> ou < ou ^) (Quantidade) (Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""

num_1 = 10
num_2 = 3
num_3 = 1
num_4 = 1150
divisao = num_1 / num_2
num_5 = 1_000_000_000
num_6 = 10_000_000
total = num_5 + num_6

# Os 2 são a mesma coisa
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')
print(f'{num_3:0>10}')  # Será preenchido de zeros, a esquerda, o tamanho total será 10 caracteres
print(f'{num_4:0^10}')
print(total)
print(f'{total:,}')
print(f'{total:_}')

nome = "Alex"
sobrenome = "Vido"
nome_formatado = '{:@>50}'.format(nome)
nome_formatado0 = '{n:@>50} {n} {n}'.format(n=nome)
nome_completo = '{0} {1}'.format(nome, sobrenome)


print(f'{nome:s}')  # Não será feito nada de diferente pois não foi definido nada diferente
print(f'{nome:#^50}')
print(nome_formatado)
print(nome_formatado0)
print(nome_completo)
print(nome.upper())
print(sobrenome.lower())
print(nome_completo.title())
