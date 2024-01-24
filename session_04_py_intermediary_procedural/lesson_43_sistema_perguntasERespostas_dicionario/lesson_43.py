import time
print('Bem vindo ao jogo de matemática!')
print('Para responder, digite a letra da resposta correta')
time.sleep(0.7)

respostas_certas = 0

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            'd': '2'
        },
        'resposta certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 * 5?',
        'respostas': {
            'a': '20',
            'b': '30',
            'c': '25',
            'd': '55'
        },
        'resposta certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10 / 2?',
        'respostas': {
            'a': '2',
            'b': '10',
            'c': '5',
            'd': '2'
        },
        'resposta certa': 'c',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 150 - 35?',
        'respostas': {
            'a': '120',
            'b': '115',
            'c': '100',
            'd': '110'
        },
        'resposta certa': 'b',
    }
}

print()

for pk, pv in perguntas.items():
    print()
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta certa']:
        print('Ebaaaa, você acertou!!!')
        respostas_certas += 1
        time.sleep(0.7)
    else:
        print('Xiiii, você errou!')
        time.sleep(0.7)
    print()

qtd_perguntas = len(perguntas)
porcentagem = respostas_certas / qtd_perguntas * 100
porcentagem = int(porcentagem)

if respostas_certas == 1:
    print(f'Você acertou {respostas_certas} pergunta')
else:
    print(f'Você acertou {respostas_certas} perguntas')

print(f'Você acertou {porcentagem}% das perguntas')
