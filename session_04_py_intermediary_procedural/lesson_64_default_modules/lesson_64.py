'''
Default modules in Python:
Modules are files .py (Contain Python code) and serve to expand the default functionalities
of the language
See all the default modules of the Python in:
https://docs.python.org/3/py-modindex.html
'''

from sys import platform as so
# import random
# from random import *  # Assim importa tudo, porém a chances de sobreescrever algo é grande
from random import randint
print(so)

for i in range(10):  # Para executar 10 vezes o comando abaixo
    # print(random.randint(0, 10))
    print(randint(0, 10))
