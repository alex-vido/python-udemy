"""
Operadores Relacionais
== Igualdade
> Maior que
>= Maior ou igual que
< Menor
<= Menor ou igual
!= Diferente
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
idade_minima = 18
idade_maxima = 40

if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} pode pegar emprestimo')

else:
    print(f'{nome} não pode pegar empréstimo')
