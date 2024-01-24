from random import randint

class Person:
    actual_year = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_year_birth(self):
        print(self.actual_year - self.age)

    @classmethod
    def for_year_birth(cls, name, year_birth):
        age = cls.actual_year - year_birth
        return cls(name, age)

    @staticmethod
    def gen_id():
        rand = randint(10000, 19999)
        return rand


p1 = Person('Alex', 29)
p2 = Person('Kelly', 28)

# p3 = Person.for_year_birth('Guilherme', 2010)
p3 = Person('Arthur', 8)
print(p3)
print(p3.name, p3.age)
p3.get_year_birth()

print(p1.gen_id())
