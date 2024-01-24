# Setter = configuring a valueu (=)
# Getter = obtain a value (.)

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        print('Setter')
        self._name = name

    @property
    def sobrenome(self):
        return 'Desconhecido'


p1 = Person('Kelly')
print(p1.name)
print(p1.sobrenome)
