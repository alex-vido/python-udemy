'''
count - Itertools
'''
from itertools import count

counter = count(start=5, step=0.05)  # Negarivo ex: start=-1, step=-1

for value in counter:
    print(round(value, 2))

    if value >= 10 or value <= -10:
        break
