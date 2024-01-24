"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05
042520110001
0   4   2   5   2   0   1   1   0   0   0   1   X   X
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65 ##
Fórmula -> 11 - (65 % 11) = 1
Primeiro Digito = 1

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67 ##
Fórmula -> 11 - (67 % 11) = 11 (Como o resultado é maior que 9, então é 0)
Segundo Digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original = 04.252.011/0001-10
Válido

"""

"""
Passo a passo:
Remover caracteres
validar se possui
Remover os 2 últimos digitos
Transformar em int

Criar um laço ir fazer a multiplicação
depois somar todos os números
dividir pela formula gerar o primeiro numero
Repetir os passos desse 2 bloco porém com o primeiro digito

Comparar o cnpj criado com o cnpj original
"""

import cnpj

cnpj_original = cnpj.remove_caracters('71.506.168/0001-11')
cnpj_first_validation = cnpj.cnpj_digits_validation(cnpj_original)
cnpj_without_digits = cnpj_original[:-2]

first_d = cnpj.first_dig(cnpj_without_digits)

new_cnpj = cnpj.sec_d(first_d)


def cnpj_validator(cnpj):

    sequence = cnpj == str(cnpj[0]) * len(cnpj)

    if cnpj == cnpj_original and not sequence:
        return 'CNPJ Válido'
    else:
        return 'CNPJ Inválido'


print(cnpj_validator(new_cnpj))
