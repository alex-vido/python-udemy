"""
For / Else
"""
variavel = ['Alex Vido', 'Kelly Vido', 'Guilherme', 'Arthur', 'Enzo', 'Pedro', 'Yuri']

"""
for valor in variavel:
    print(valor)
    continue  # Executará o prox laço, sem exec a continuação do laço atual
    # break  # Finaliza o laço
    print(valor)

for valor in variavel:
    if valor.startswith('K'):
        print(f'Começa com K: {valor}')
    else:
        print(f'Não começa com K: {valor}')
"""

comeca_com_k = False
for valor in variavel:
    if valor.lower().startswith('k'):
        comeca_com_k = True

if comeca_com_k:
    print('Existe uma palavra que começa com K')
else:
    print('Não existe uma palavra que começa com K')
