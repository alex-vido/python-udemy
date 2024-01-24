name = 'Alex Vido'

# iterator == ger
iterator = iter(name)
ger = (letter for letter in name)
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except:
    pass

print('Cadê os valores?')

for valor in iterator:
    print(valor)

'''
for letter in name:
    print(letter)

print('#' * 80)

for letter in name:

    print(letter)

print(name)
'''
