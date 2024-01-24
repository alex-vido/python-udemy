try:  # Todo esse bloco try é para conseguir importar um módulo anterior/atrás.
    # Se retirarmos o bloco try, funcionará apenas na pasta principal (o que nesse caso é o único local importante)
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
                # '../../'  # 2 pastas atrás
            )
        )
    )
except ImportError:
    raise


from lesson_68_package_1.module_1 import v_1

v_2 = 'var_2'

print(v_1)
