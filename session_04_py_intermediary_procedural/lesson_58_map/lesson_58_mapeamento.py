from session_03_py_intermediary_procedural.lesson_58_map.lesson_58_dados import pessoas, produtos, lista

# Isso
# nova_lista = map(lambda x: x * 2, lista)  # Retorna um iterador
# print(list(nova_lista))

# Igual a isso
nova_lista = [x * 2 for x in lista]
print(nova_lista)

nl = '\n'
print(f'{nl}', '#' * 120, f'{nl}')


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)

print(f'{nl}', '#' * 120, f'{nl}')


def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


idades = map(aumenta_idade, pessoas)

for idade in idades:
    print(idade)
