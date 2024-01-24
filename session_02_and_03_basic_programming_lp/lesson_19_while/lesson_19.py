"""

n = 0
while n < 10:
    if n == 3:  # Não dará print no 3, e não execuará o laço abaixo devido o continue, até que o valor seja != 3
        n += 1
        continue
        # break
    print(n)
    n += 1

print('Acabou!')

x = 0
y = 0

while x < 10:

    y = 0

    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x += 1

print('Acabou!')

"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input(('Deseja sair? [s]im ou [n]ão: '))

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operação inválida!')
