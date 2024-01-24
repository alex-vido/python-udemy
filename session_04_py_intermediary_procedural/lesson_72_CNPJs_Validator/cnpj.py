import re


def remove_caracters(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def cnpj_digits_validation(cnpj):
    if cnpj.isnumeric() and len(cnpj) == 14:
        return cnpj
    else:
        print('CNPJ must be a 14 numbers sequence')


def first_dig(cnpj):
    reverse = 5
    total = 0

    for i in range(12):

        total += int(cnpj[i]) * reverse

        reverse -= 1

        if reverse < 2:
            reverse = 9

    d = 11 - (total % 11)

    if d > 9:
        d = 0
    cnpj += str(d)
    return cnpj


def sec_d(cnpj):
    reverse = 6
    total = 0

    for index in range(13):

        total += int(cnpj[index]) * reverse

        reverse -= 1

        if reverse < 2:
            reverse = 9

    d_2 = 11 - (total % 11)

    if d_2 > 9:
        d_2 = 0

    cnpj += str(d_2)
    return cnpj
