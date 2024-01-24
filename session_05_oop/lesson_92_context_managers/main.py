"""
file = open('abc.txt', 'w')
file.write('Something')
file.close()
"""

"""
with open('abc.txt', 'w') as file:
    file.write('Something')
"""

"""
class File:
    def __init__(self, file, mode):
        print('Opening the file')
        self.file = open(file, mode)

    def __enter__(self):
        print('Returning the file')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Closing the file')
        self.file.close()
        # Exception treated
        return True

with File('abc.txt', 'w') as file:
    file.write('Something')
"""

from contextlib import contextmanager


@contextmanager
def to_open(file, mode):
    try:
        print('Opening file')
        file = open(file, mode)
        yield file  # Used yield because return not execute the finally
    finally:
        ('Closing file')
        file.close()


with to_open('abc.txt', 'w') as file:
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')
