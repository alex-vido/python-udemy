class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__

    def talk(self):
        return f'{self.class_name} Talking...'


class Client(Person):
    def buy(self):
        print(f'{self.class_name} is buying')


class Student(Person):
    def study(self):
        print(f'{self.class_name} is studying')
