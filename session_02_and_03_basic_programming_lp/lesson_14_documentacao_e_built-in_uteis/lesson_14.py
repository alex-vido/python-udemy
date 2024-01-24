import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)


num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')




# Essa é a forma original do Python

# isnumeric isdigit isdecimal
# números inteiros e positivos
print(num1.isnumeric())  # Vai verificar se o que foi digitado pode ser convertido para numero
print(num2.isnumeric())

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Não foi possível converter os números')
    
"""
# Essa é com a do professor, que valida também float
print(is_number(num1))  # Vai verificar se o que foi digitado pode ser convertido para numero
print(is_number(num2))

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
else:
    print('Não foi possível converter os números')
    
"""
