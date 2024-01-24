"""
Desempacotamento de listas
"""
"""
lista = ['Luiz', 'João', 'Maria']
n1, n2, n3 = lista
print(n2)
"""
lista = ['Maria', 'João', 'José', 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
n1, n2, *outra_lista, ultimo_da_lista = lista
# *outra_lista pegou todos os outros valores, porém após a virgula,
# pegará o último ou os últimos, se criar mais variaveis

# Se fizer por ex: n1, n2, *_ criará uma nova var normal, porem por convenção indica que não usará os valores

print(n1, n2)
print(outra_lista)
print(ultimo_da_lista)
