"""
Funções (def) - *args **kwargs
kwargs são keyword args ex: nome='Alex'
"""

# A partir do momento que seta um valor padrão para um argumento, precisará obrigatóriamente setar valorers dos próximos
def funcao(arg_1, arg_2, arg_3, arg_4, arg_5, nome=None, arg_6=None):
    print(arg_1, arg_2, arg_3, arg_4, arg_5, nome, arg_6)
    return nome, arg_6  # Sem return o valor da var é None
# Com return ele retorna uma tupla

# A partir do momento que setou um valor, precisa seta-lo também ao chamar
var = funcao(1, 2, 3, 4, 5, nome='Alex', arg_6=6)
print(var)

def func(*args, **kwargs):  # Para quando você não sabe quantos argumentos precisam ser retornados. Isso é uma tupla
    # args = list(args)  # Para transformar em lista
    # args[0] = 20  # Só funciona em lista, em tuplas não
    print(args)
    print(kwargs)

    nome = kwargs.get('nome')
    print(nome)
    # idade = ['idade']
    idade = kwargs.get('idade')  # É muito melhor usar get quando não tem certeza se o arg existe

    if idade is not None:
        print(idade)


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]
func(*lista_1, *lista_2, nome='Alex', sobrenome='Vido')
# * Desempacotou a lista, senão seria uma lista dentro de uma tupla, e se add algo ficaria fora da lista
