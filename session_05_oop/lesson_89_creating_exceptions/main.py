class IsWrongError(Exception):
    pass


def test():
    raise IsWrongError('Wrong!')

try:
    test()
except IsWrongError as error:
    print(f'Error {error}')
