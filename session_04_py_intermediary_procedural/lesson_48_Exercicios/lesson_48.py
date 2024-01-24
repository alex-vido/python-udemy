# pegar a var string e separar em listas de 0 a 9, e depois criar um retorno de todos eles, porém separado com ponto
string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
li = [string[i:i + n] for i in range(0, len(string), n)]
print(li)
li_2 = '.'.join(li)
print(li_2)
print('###############################################################################')
"""
Explicação mais detalhada
"""
tuples = [(i, i + n) for i in range(0, len(string), n)]
list_1 = [string[i:i + n] for i in range(0, len(string), n)]
raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
return_1 = '.'.join(list_1)
print(tuples)
print(list_1)
print(raw)
print(return_1)

'''
Tá, da uma olhada nesse código feito à mão... é exatamente isso (só que de 2 em 2):

    # ìndices 0123456
    string = 'Mariana'

    print(string[0:2], end='-')
    print(string[2:4], end='-')
    print(string[4:6], end='-')
    print(string[6:8])
    # Saída: Ma-ri-an-a

Percebe os ranges que estou capturando? De 2 em 2, 0-2, 2-4, 4-6, etc, etc... Esses ranges me dão
o fatiamento da string. Ex.: 0:2 (Ma), 2:4 (ri), etc... Lembre-se que o fatiamento não captura
o último número, então 0 a 2, seria Mar, mas o 2 não é incluído, então Ma. Assim vai até o final.

Nós sabemos que a função range, pode receber um parâmetro step (passo), que informa de
quantos em quantos valores vamos pular.

    [indice for indice in range(0, 8, 2)]  # [0, 2, 4, 6]

Veja que o range começa em 0, termina em 8 e pula de 2 em 2.

Com isso, temos as primeiras casas dos ranges de fatiamento... Agora falta a parte do final,
o primeiro deveria ser 0-2, segundo 2-4, etc, etc...

Então podemos somar 2 em cada índice. Veja:

    # ['0-2', '2-4', '4-6', '6-8']
    print([f'{indice}-{indice + 2}' for indice in range(0, 8, 2)])

Agora temos os ranges corretos... é só mandar esses mesmos valores no fatiamento da string,
assim como fiz manualmente no início:

    # ìndices 0123456
    string = 'Mariana'

    # ['Ma', 'ri', 'an', 'a']
    print([string[indice: indice + 2] for indice in range(0, 8, 2)])

Agora podemos fazer o que quisermos, por exemplo, adicionar traços.

    # ìndices 0123456
    string = 'Mariana'

    # ['Ma', 'ri', 'an', 'a']
    dois_em_dois = [string[indice:indice + 2] for indice in range(0, 8, 2)]

    # Unindo tudo
    print('-'.join(dois_em_dois))  # Ma-ri-an-a

Em um cenário totalmente automatizado ficaria:

    # ìndices 0123456
    string = 'Mariana'

    step = 2
    dois_em_dois = [
        string[indice:indice + step]
        for indice in range(0, len(string), step)
    ]

    # Unindo tudo
    print('-'.join(dois_em_dois))  # Ma-ri-an-a
'''
