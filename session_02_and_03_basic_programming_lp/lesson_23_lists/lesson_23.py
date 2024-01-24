"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
"""
lista = ['A', 'Bacana', 'C', 'D', 'E', -10.5]

strings = 'ABCDE'
print(strings[1])
print(lista[0:3])  # Vai até o índice 2
print(lista[:3])  # Do começo até o indice 2
print(lista[2:])  # Vai do indice 2 até o final
print(lista[::2])  # Do começo até o final pulando de 2 em 2
print(lista[::-1])  # Inverte a lista
"""
"""
l1 = list(range(1, 10))
l2 = [4, 5, 6]
l3 = ['Alex', 1, 32.5, True]
soma = 0
"""
"""
l1.extend(l2)
l2.append('a')  # Adiciona por último
l2.insert(0, 'Banana')
l2.pop()  # Remove o último indice

  del(l1[3:5])  # Excluiu do índice 3 ao 4
for valor in l1:
    soma = soma + valor
print(l1)
print(soma)

for elem in l3:
    print(f'O tipo do elemento {elem} é {type(elem)}')
"""

secreto = 'alex'
digitadas = []
chances = 5

while True:
    if chances < 1:
        print('Você perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhuul, a letra "{letra}" existe na palavra secreta')
    else:
        print(f'Aff, a letra {letra.upper()} NÃO existe na palavra secreta')
        digitadas.pop()
        chances -= 1
        print(f'Você possui mais: {chances} chances. ')

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra secreta é: {secreto.upper()}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')
