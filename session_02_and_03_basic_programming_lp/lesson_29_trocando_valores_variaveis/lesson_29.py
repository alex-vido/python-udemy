# Invertendo valores
from ast import YieldFrom


x = 10  # 'Vido'
y = 'Alex'  # 10
z = 'Vido'  # 'Alex'
x, y, z = z, x, y
print(f'x = {x}, y = {y}, z = {z}')
