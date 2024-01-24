frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

"""
while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    contador += 1
print(nova_string)

"""

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

# Iteração <-  Iterar é o ato de percorrer cada um dos elementos da sua str ou elemento iteravel
while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
