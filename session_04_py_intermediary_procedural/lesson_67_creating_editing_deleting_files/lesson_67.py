# https://docs.python.org/3/library/functions.html#open

"""
file = open('abc.txt', 'w+')
file.write('Line 1\n')
file.write('Line 2\n')
file.write('Line 3\n')

file.seek(0, 0)
print('Read lines')
print(file.read())

print('\n', '#' * 120, '\n')

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')

print('\n', '#' * 120, '\n')

file.seek(0, 0)
print(file.readlines())

print('\n', '#' * 120, '\n')

file.seek(0, 0)
for line in file:
    print(line, end='')

file.close()
"""
"""
try:
    file = open('abc.txt', 'w+')
    file.write('Line')
    file.seek(0)
    print(file.read())
finally:
    file.close()
"""

# w+ clean the file, write. + update

import os

# Pathonic form
with open('abc.txt', 'w+') as file:  # Close isn't necessary, with this context manager
    file.write('Line 1\n')
    file.write('Line 2\n')
    file.write('Line 3\n')

    file.seek(0)
    print(file.read())

with open('abc.txt', 'a+') as file:  # write. Append to the final of the file if it exists
    file.write('Line 4\n')
    file.write('Line 5\n')
    file.write('Line 6\n')

    file.seek(0)
    print(file.read())

with open('abc.txt', 'r') as file:  # Read
    print(file.read())

os.remove('abc.txt')  # Remove the file

import json

d1 = {
    'Person 1': {
        'name': 'Alex',
        'years': 29
    },
    'Person 2': {
        'name': 'Kelly',
        'years': 28
    }
}

d1_json = json.dumps(d1, indent=True)  # json file, with indentation

with open('abc.json', 'w+') as file:
    file.write(d1_json)
