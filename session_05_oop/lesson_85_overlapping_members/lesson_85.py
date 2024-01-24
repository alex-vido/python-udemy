from classes import Person, Client, Student, ClientVIP

"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

c1 = Client('Alex', 29)
print(c1.name)
c1.talk()
c1.buy()
print()

s1 = Student('Kelly', 28)
print(s1.name)
s1.talk()
s1.study()

c2 = ClientVIP('Rose', 25, 'Djumble')
c2.talk()
