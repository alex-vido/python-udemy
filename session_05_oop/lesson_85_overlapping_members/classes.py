class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.class_name = self.__class__.__name__

    def talk(self):
        print(f'{self.class_name} Talking...')


class Student(Person):
    def study(self):
        print(f'{self.class_name} is studying')


class Client(Person):
    def buy(self):
        print(f'{self.class_name} is buying')

    def talk(self):
        print("I'm in client")


class ClientVIP(Client):
    def __init__(self, name, age, lastname):
        Person.__init__(self, name, age)
        self.lastname = lastname

    def talk(self):
        # super().talk()
        Person.talk(self)
        Client.talk(self)
        print(f'{self.name} {self.lastname} is talking...')
