"""
Split, Join, Enumerate
* Split - Dividir uma String  # str
* Join - Juntar uma lista  # str
* Enumerate - Enumerar elementos da lista  # list / iterables
"""

string = 'O Brasil é o país do futebol, o Brasil é penta'
lista_1 = string.split(' ')  # Transformará a frase em uma lista
lista_2 = string.split(',')
lista_3 = ' '.join(lista_1)  # Transformará a lista em frase
print(lista_3)
# print(lista_1)
# print(lista_2)

palavra = ''
contagem = 0

for valor in lista_1:
    # print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista_2:
    print(valor.strip().capitalize())  # strip remove espaço do ínicio e fim das frases. Cap deixa a 1 palavra maiuscula


for indice, valor in enumerate(lista_1):
    print(indice, lista_1[indice])

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for v in lista:
    print(v)  # igual a print(v[0], v[1])

# lista_4 == lista_5

"""
lista_4 = [
    [0, 'Alex'],
    [1, 'Kelly'],
    [2, 'Filhos']
]
for indice, nome in lista_4:
    print(indice, nome)
"""

lista_5 = ['Alex', 'Kelly', 'Filhos']

for indice, nome in enumerate(lista_5):
    print(indice, nome)
