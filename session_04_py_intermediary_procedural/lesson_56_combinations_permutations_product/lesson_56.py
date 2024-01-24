'''
Combinations, permutations e Product - Itertools
Combinations - Ordem não importa
Permutation - Ordem importa
Ambos não repetem valores únicos
Product - Ordem importa e repete valores únicos
'''

from itertools import combinations, permutations, product


family = ['Alex', 'Kelly', 'Guilherme', 'Arthur', 'Enzo Gabriel', 'Pedro Rubens', 'Yuri']

# for group in combinations(family, 2):  # Se tem Alex e Kelly não terá Kelly e Alex
#     print(group)

# for group in permutations(family, 2):  # Terá todas as cominações ex: Alex e Kelly, Kelly e Alex
#    print(group)

for group in product(family, repeat=2):  # Repete até valores únicos como Alex e Alex
    print(group)
