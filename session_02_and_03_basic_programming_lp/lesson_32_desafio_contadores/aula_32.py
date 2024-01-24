"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""


for p, r in enumerate(range(10, 1, -1)):
    print(p, r)

print()
print('######################################')
print()

index = 0
valor = 10

while index < 9:
    print(index, valor)
    index += 1
    valor -= 1
