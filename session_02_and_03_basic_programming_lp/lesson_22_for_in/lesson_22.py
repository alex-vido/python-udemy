"""
For in em Python
Iterando Strings com for
Função range(start=0, stop, step=1)
"""

# continue == pula para o próximo passo
# break == termina o laço

texto = 'Python'
nova_string = ''
"""
c = 0

while c < len(texto):
    print(texto[c])
    c += 1
"""

for letra in texto:
    if letra == 't':
        continue
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)

print('####################################################################')

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)

print('####################################################################')

for letra in texto:
    print(letra)

print('####################################################################')

for i, letra in enumerate(texto):
    print(i, letra)

print('####################################################################')

for n in range(10):  # Aqui omitimos o inicio e o step. Começará do 0, terminará no 9, e pulará de 1 em 1
    print(n)

print('####################################################################')

for n in range(5, 10):
    print(n)

print('####################################################################')

for n in range(0, 100, 5):  # Inicie no 0, terminei no 100 e pule de 5 em 5.
    print(n)

print('####################################################################')

for n in range(20, 10, -1):  # Inicie no 0, terminei no 100 e pule de 5 em 5.
    print(n)

print('####################################################################')

# Esse é igual ao debaixo
for n in range(100):
    if n % 8 == 0:
        print(n)
print()
for n in range(0, 100, 8):
    print(n)

print('####################################################################')
