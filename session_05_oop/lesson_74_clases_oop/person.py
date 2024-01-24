from datetime import datetime

class Person:
    actual_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, eating=False, talking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.talking = talking

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
            return

        print(f'{self.name} is eating {food}.')
        self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f"{self.name} isn't eating.")
            return

        print(f'{self.name} stop eating.')
        self.eating = False

    def talk(self, subject):
        if self.eating:
            print(f"{self.name} please don't speaking while eating.")
            return

        if self.talking:
            print(f'{self.name} is talking.')
            return

        print(f'{self.name} is talking about {subject}')
        self.talking = True

    def stop_talk(self):
        if not self.talking:
            print(f"{self.name} isn't talking.")
            return

        print(f'{self.name} stop talk')

    def get_year_birth(self):
        return self.actual_year - self.age
