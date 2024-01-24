from session_03_py_intermediary_procedural.lesson_59_filter.lesson_58_dados import pessoas, produtos, lista
'''
Map = Mapa
Filter = Filtro

Map é usado para mapear cada valor de uma lista para outro valor qualquer. Isso quer dizer que
 o tamanho da lista sempre será o mesmo, ela sempre vai ter o mesmo número de elementos da lista original.
 Mapear significa mais ou menos falar que o índice 0 da lista original, será convertido
 para qualquer outro valor no índice 0 da nova lista.

    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    lista_mapeada = map(lambda item: item * 2, lista)
    print(list(lista_mapeada))  # [2, 4, 6, 8, 10, 12, 14, 16]

Filter é usado para filtrar valores, isso quer dizer que a nova lista poderá ter o mesmo tamanho
da lista original ou pode ser menor... Por exemplo:

    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    # Filtrando valores entre 3 e 6
    lista_filtrada = filter(lambda item: item >= 3 and item <= 6, lista)
    print(list(lista_filtrada))  # [3, 4, 5, 6]

Nesse caso, a nova lista pode até estar vazia se nenhum filtro passar, como em:

    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    # Filtrando a letra 'a'
    lista_filtrada = filter(lambda item: item == 'a', lista)
    print(list(lista_filtrada))  # []
'''


'''
nova_lista = filter(lambda x: x > 5, lista)  # Esse
nova_lista_comp = [x for x in lista if x > 5]  # Igual a esse
print(list(nova_lista))
print(nova_lista_comp)
'''

def filtra_preco(produto):
    if produto['preco'] > 50:
        return True

# nova_lista = filter(lambda p: p['preco'] > 50, produtos)
nova_lista = filter(filtra_preco, produtos)

for produto in nova_lista:
    print(produto)

print('\n', '#' * 120, '\n')

def filtra_idade(pessoa):
    if pessoa['idade'] >= 18:
        return True

lista_pessoas = filter(filtra_idade, pessoas)
for pessoa in lista_pessoas:
    print(pessoa)
