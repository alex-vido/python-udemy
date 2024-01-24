
lst = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
]

# This, but upper isn't possible with dict()
d1 = {x.upper(): y.upper() for x, y in lst}
# Same of this
# d1 = dict(lst)
print(type(d1), d1)

d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

d3 = {f'Key_{x}': x ** 2 for x in range(5)}
print(d3)
