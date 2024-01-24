usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")

else:
    print('Você foi cadastrado no sistema')

string1 = input("Digite alguma coisa: ")
string2 = input("Digite outra coisa: ")
print(f'A quantidade total de caracteres digitado foi: {len(string1) + len(string2)}')

print(len(string1) == string1.__len__())  # True

# Não funciona com números, nem Boolean
