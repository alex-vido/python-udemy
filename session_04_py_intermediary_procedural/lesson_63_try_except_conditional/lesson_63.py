from tokenize import Number


def convert_number(value):
    try:
        value = int(value)
        return value
    except ValueError:
        try:
            value = float(value)
            return value
        except ValueError:
            pass


n_1 = convert_number(input('Digite um número: '))
n_2 = convert_number(input('Digite outro número: '))

if n_1 is None or n_2 is None:
    print('Erro: Isso não é número')
else:
    print(n_1 * n_2)
