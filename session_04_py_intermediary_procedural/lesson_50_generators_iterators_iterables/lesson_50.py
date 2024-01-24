from codecs import latin_1_decode
import sys
import time
from tkinter import Variable

'''
lst = [0, 1, 2, 3, 4, 5]
lst_1 = list(range(100))
print(sys.getsizeof(lst_1))  # How many bytes

# This
for v in lst:  # v transform the list in iterator
    print(v)

# Do that
lst = iter(lst)  # transform the list in iterator

print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))
print(next(lst))

print(hasattr(lst, '__iter__'))  # Has a itterable?
print(hasattr(lst, '__next__'))  # Is a iterable?

'''

# Simulating the delay in this process, because, first the function, add all value in r, to after show value in r
def no_gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

ng = no_gera()

for v in ng:
    print(v)

# Generator
# Generator show the value without delay add all the values.
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)

def gera_1():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

ge = gera_1()

for v in ge:
    print(v)

l1 = [x for x in range(100000)]  # 800984 bytes
print(type(l1), sys.getsizeof(l1))
l2 = (x for x in range(100000))  # 104 bytes, never change
print(type(l2), sys.getsizeof(l2))
