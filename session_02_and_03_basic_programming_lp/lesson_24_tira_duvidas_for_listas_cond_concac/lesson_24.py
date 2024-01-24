secreto = 'python'
secreto_temporario = ''

digitadas = ['n', 'o', 'p', 'i', 'l', 'h', 't', 'y']

for letra_secreta in secreto:
    print(f'Iteração para letra {letra_secreta}')

    if letra_secreta in digitadas:
        print(f'Eba, a letra que eu queria: {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        print(f'Não era a letra que eu queria: {letra_secreta}')
        secreto_temporario += '*'
    print(f'secreto_temporario = {secreto_temporario}')
print()
print(secreto_temporario)

if secreto_temporario == secreto:
    print('Você ganhou')
