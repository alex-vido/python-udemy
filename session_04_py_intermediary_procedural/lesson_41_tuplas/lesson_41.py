'''
Principal diferença entre listas e tuplas é que tuplas não pode alterar seus elementos
'''

t1 = (1, 2, 3, 4, 'Alex', 13.3423)
t2 = 5, 6, 7, 8, 'Vido', 25.653
t3 = 5,

t4 = t1 + t2 + t3

n1, n2, n3, *_, n10 = t4  # Desempacotando

t5 = (50, 30, 'Alex') * 20

t6 = 10, 20, 30
t6 = list(t6)  # Convertendo tuplas em listas
t6[1] = 3000
# t6 = tuple(t6)  # Convertendo em tuplas novamente

print(type(t1))  # <class 'tuple'>
print(t1[4])

for v in t1:
    print(v)

print('######################################################')

print(type(t2))
print(t2)

print('######################################################')

print(type(t3))
print(t3)

print('######################################################')

print(type(t4))
print(t4)

print('######################################################')

print(type(n3))
print(n3)

print('######################################################')

print(type(t5))
print(t5)

print('######################################################')

print(type(t6))
print(t6)
