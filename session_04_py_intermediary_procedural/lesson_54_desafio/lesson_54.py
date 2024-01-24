'''
Somar 2 listas de int ou float (lista A e lista B) retornando uma nova lista com os valores somados

Se uma lista for menor que a outra, só considerará o tamanho da lista menor

Ex:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
=================================
lista_soma = [2, 4, 6, 8]
'''

# Meu passo a passo
# Transformar em zip para remover os valores a mais
# criar lista_soma com um list comprehesion de somar valores armazenando os resultados nela

# CONSEGUI FAZER UM EXERCICIO SOZINHO UHUUUUUUUUUUUUUUUUL
# Minha solução
from itertools import zip_longest


list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
list_zip = zip(list_a, list_b)
list_sum = [(x + y) for x, y in list_zip]
print(list_sum)

# Solução prof
lista_soma = [(x + y) for x, y in zip(list_a, list_b)]
print(lista_soma)

# Solução genérica do prof
lista_soma_1 = []
lista_soma_2 = []


for i in range(len(list_b)):
    lista_soma_1.append(list_a[i] + list_b[i])
print(lista_soma_1)

# Solução Python 1
for i, _ in enumerate(list_b):
    lista_soma_2.append(list_a[i] + list_b[i])
print(lista_soma_2)

# Com todos os valores, porém sem somar os assimétricos
lista_soma_3 = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]
print(lista_soma_3)
