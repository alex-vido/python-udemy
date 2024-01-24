import copy

d1 = {'chave_1': 'valor da chave'}
d1['nova_chave'] = 'valor da nova chave'

d2 = dict(chave_3='valor da chave')

d3 = {
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'Tupla'
}

if d1.get('nome_da_chave') is not None:
    print(d1.get('nome_da_chave'))

print(type(d1))
print(d1)
print(d2)
print(d3[(1, 2, 3, 4)])
print('str' in d3)
print('str' in d3.keys())
print('valor' in d3.values())

print('############################################')

for k, v in d3.items():
    print(k, v)

print('############################################')

clientes = {
    'cliente_1': {
        'nome': 'Alex',
        'sobrenome': 'Vido'
    },
    'cliente_2': {
        'nome': 'Kelly',
        'sobrenome': 'Vido'
    },
    'cliente_3': {
        'nome': 'Yuri',
        'sobrenome': 'Vido'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

print('############################################')

d4 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 'd': ['Alex', 'Vido']}
v = d4.copy()  # Os valores são uma cópia raza / uma referência
v[1] = 'Alex'
v['d'][0] = 'Joãozinho'  # Quando acessa o valor de uma chave, ele altera também na original
print(f'v_1: {v}')
v['d'] = ('Vido', 'Alex')
print(f'v_2 {v}')
z = copy.deepcopy(d4)  # Precisou fazer um import copy
z['d'][1] = 'Barbosa'

print(f'v["d"][0] {v["d"][0]}')

print(f'Cópia raza {d4}')

print(f'Cópia profunda {z}')

# clientes.popitem()  # Para apagar o ultimo da lista:
clientes.pop('cliente_3')  # Para apagar um item
print(clientes)

d1.update(d3)  # Para concatenar dicionários
print(d1)
