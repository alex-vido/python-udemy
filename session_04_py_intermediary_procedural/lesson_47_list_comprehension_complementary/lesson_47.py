
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# novos_numeros = numeros  # Isso não é uma cópia, é apenas uma referencia. As 2 apontam para o mesmo local na memória
new_numbers = [number for number in numbers]  # Copy with list comprehension
print(new_numbers)
print()

another_if = [
    number
    if number != 6 else 600
    for number in numbers
    if number % 2 == 0
]

print(another_if)
print()

lines_n_columns = [
    (x, y)
    if y != 2 else (x * 1000, y * 1000)  # All X and Y == 2 will multiplied as thousand
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2  # 2 not appear on the list
]

print(lines_n_columns)
print()

# Strings

string = 'Alex Vido'
number_of_letters = 2
# new_string = ''.join([letter for letter in string])  # mapped each letter, and join
new_string = '.'.join([
    string[index: index + number_of_letters]
    for index in range(0, len(string), number_of_letters)
])

print(new_string)
print()

# Lists
names = ['alex', 'kelly', 'guilherme', 'arthur', 'enzo', 'pedro', 'yuri']
new_names = [
    f'{name[:-1].lower()}{name[-1].upper()}'  # Uppercasing the last word of each name
    for name in names
]
print(new_names)
print()

numbers_2 = [[number, number ** 2] for number in range(10)]
flat = [y for x in numbers_2 for y in x]
print(numbers_2)
print(flat)
