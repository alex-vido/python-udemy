"""
Enumerate - Enumerar elementos da lista
Enumera os indices de uma lista
"""
lista = [
    #  0       1       2
    ['Edu', 'joão', 'Luiz'],  # 0
    ['Jorge', 'Samuel', 'Regina'],  # 1
    ['Felipe', 'Fernando', 'Rogério']  # 2
]

print()
print(lista[1][2])  # Regina

print()
print('#####################################################')
print()

enumerada = enumerate(lista)
enumerada_1 = list(enumerate(lista))
print(enumerada)  # Output: <enumerate object at 0x7fbf0bae8880>  # Referencia de memória

print()
print('#####################################################')
print()

print(list(enumerada))  # Output abaixo:

"""
[ <- Lista com objeto Enumerate
    Os parenteses são tuplas
     0  1
    (0, ['Edu', 'joão', 'Luiz']),  # 0

     1  1   0        1         2
    (1, ['Jorge', 'Samuel', 'Regina']),  # 1
    (2, ['Felipe', 'Fernando', 'Rogério'])  # 2
]
"""
print()
print('#####################################################')
print()

print(enumerada_1[0][1])  # 'Edu', 'João', 'Luiz'

print()
print('#####################################################')
print()

print(enumerada_1[1][1][2])  # 'Regina'

print()
print('#####################################################')
print()
for v1, v2 in enumerate(lista, 53):
    print(v1, v2)

print()
print('#####################################################')
print()

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome_1, nome_2, nome_3 = minha_lista
    print(nome_1, nome_2, nome_3)

print()
print('#####################################################')
print()
