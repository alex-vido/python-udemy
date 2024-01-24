'''
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (Todos os elementos presentes nos 2 sets)
difference - (Elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos 2 sets, mas não em ambos)
'''
# Diferença em criar um set de dicionário, é que set só tem valor e não chaves
# Set suporta apenas elementos imutáveis, numbers, strings, tuplas
# Set não tem indice
# Set sempre aparece fora de ordem
# Set elimina elementos duplicados da lista

s1 = {1, 2, 3, 4, 5}
# s2 = {}  # Não é um set, é um dicionário
s2 = set()  # Set vazio
s2.add(6)
s2.add(7)
s2.add(8)
s2.discard(7)
s2.update('Python')  # A diferença do update para add é que o up irá iterar
s3 = set()
s3.update([1, 2, 3, 4, 5], {5, 6, 7, 8})  # Ficará em ordem e não repetirá o 5

print(type(s1))
print(s1)

for v in s1:
    print(v)

print(s2)
print(s3)

print('##########################################################')

l1 = [1, 2, 1, 1, 1, 2, 3, 1, 4, 5, 6, 7, 7, 7, 7, 8, 7, 9, 'Alex', 'Alex']
l1 = set(l1)  # Para remover itens repetidos, polrém os elem podem voltar fora de ordem
l1 = list(l1)

print(l1)
print(type(l1))

print('##########################################################')

s4 = {1, 2, 3, 4, 5, 7}
s5 = {1, 2, 3, 4, 5, 6}
# s6 = s4 | s5  # union Uniu os sets
# s7 = s4 & s5  # Todos os elementos que estão presentes nos 2 sets
# s8 = s4 - s5  # Mostrará apenas os elementos diferentes que estão no set da esquerda (s4 nesse caso)
# s9 = s4 ^ s5  # Elemtos que estão nos 2 sets, mas não em ambos (7, 6)
# print(s7)

s6 = ['Alex', 'Kelly', 'Filhos']
s7 = ['Filhos', 'Alex', 'Filhos', 'Kelly', 'Kelly', 'Kelly', 'Kelly', 'Alex', 'Filhos', 'Alex']

if set(s6) == set(s7):  # Para comparar listas com os mesmos elementos, desconsiderando os repetidos
    print('S6 é igual a S7')
