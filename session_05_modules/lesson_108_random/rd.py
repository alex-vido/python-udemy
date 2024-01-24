import random
import string

# Generate a int between A and B
intgr = random.randint(1, 40)

# Generate a int number with the function range()
i = random.randrange(900, 1000, 10)

# Generate a float between A and B
flo = random.uniform(1, 40)

# Generate a float between 0 and 1
flo_2 = random.random()

names = ['Alex', 'Kelly', 'Gui', 'Thu', 'Biel', 'Pedro', 'Yuh']
sort_names = random.choice(names)
sort_names_2 = random.choices(names, k=2)  # Can repeat the value in the choice
sort_names_3 = random.sample(names, 2)  # No repeat the choice
random.shuffle(names)

# Generate aleatory password
letters = string.ascii_letters
digits = string.digits
caracters = '!@#$%*-_=+?'
geral = letters + digits + caracters
password = "".join(random.choices(geral, k=20))

print(intgr)
print(i)
print(flo)
print(flo_2)
print(sort_names_3)
print(names)
print(password)
