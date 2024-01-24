"""
Lambda - Se fala landa
São funções anonimas
"""

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 9],
    ['P4', 50],
    ['P5', 12]
]

# sort é para sortear, se tratando de listas, o Python não saberia como sortear
# Nesse caso criamos uma função solicitando que retornasse o item[1], nesse caso os preços
# Logo ele sorteará a lista de acordo com os preços do menor para o maior, porém com reverse, será do menor para o maior
# Criamos uma expressão lamda(função anonima) para não ter que criar uma função inteira só para informar qual item é
# para ser usado no sorteio

"""
def func(item):
    return item[1]
"""

# lista.sort(key=lambda item: item[1], reverse=True)

# Dessa forma não estamos alterando a lista original
print(sorted(lista, key=lambda i: i[1], reverse=True))
