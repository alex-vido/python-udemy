from classes import Person, Client, Student

c1 = Client('Alex', 29)
print(c1.name)
print(c1.talk())
c1.buy()
print()

s1 = Student('Kelly', 28)
print(s1.name)
print(s1.talk())
s1.study()
