try:
    # a  # Name Error

    # a  = []
    # print(a[1])  # Index error

    # a = {}
    # print(a[1])  # Key error
    a = 0
    try:
        a = 1/0
    except:
        print('Erro', error)
except NameError as error:
    print('Erro:', error)
except (IndexError, KeyError) as error:
    print('Erro de index ou Key:', error)
except Exception as error:
    print('Ocorreu um erro inesperado', error)
else:
    print('Seu código foi executado com sucesso')
finally:  # Será sempre executada
    print('Finalmente...')

print('Bora continuar')
