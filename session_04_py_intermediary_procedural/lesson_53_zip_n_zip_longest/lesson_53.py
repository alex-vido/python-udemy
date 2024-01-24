'''
Zip - Unifing iterables
Zip_longest - Itertools
'''

from itertools import zip_longest, count

indice = count()
cities = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Monte belo', 'Outra']
states = ['SP', 'RJ', 'MG', 'BA']

cities_states = zip(indice, cities, states)

for v in cities_states:
    print(v)

print()
print('#' * 120)
print()

# If use count() with zip_longest probably will do a infinite loop
c_s_1 = zip_longest(cities, states, fillvalue='Estado')
for c, s in c_s_1:
    print(f'{s} - {c}')
