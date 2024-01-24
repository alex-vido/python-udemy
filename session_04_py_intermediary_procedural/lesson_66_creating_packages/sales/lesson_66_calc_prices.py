"""
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
"""

from sales.format_value import lesson_66_format as brl


def increase(value, percentage, format_value=False):
    r = value + (value * (percentage / 100))
    if format_value:
        return brl.format_to_brl(r)
    else:
        return r


def decrease(value, percentage, format_value=False):
    r = value - (value * (percentage / 100))
    if format_value:
        return brl.format_to_brl(r)
    else:
        return r
