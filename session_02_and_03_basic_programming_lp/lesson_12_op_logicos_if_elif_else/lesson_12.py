"""

Operadores lógicos
and, or, not
in e not in


a = 2
b = 2
c = 3
d = ""  # Vazio é considerado um bool false
e = 0  # 0 tambémé considerado um boolean False
nome = 'Alex'

print(a == b and b < c)  # True
print(a == b or b < c)  # True
print(not c < a)  # True'

if not d:
    print("Digite um valor na var d")

if 'le' in nome:
    print("Existe a letra le no nome")

"""

usuario = input("Digite o usuário: ")
senha = int(input("Digite sua senha: "))
usuario_bd = 'alex'
senha_bd = 1207

if usuario == usuario_bd and senha == senha_bd:
    print('Você está logado no sistema')

else:
    print('Usuário ou senha inválidos')
