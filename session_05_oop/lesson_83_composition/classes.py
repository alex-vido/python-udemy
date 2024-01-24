class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.adresses = []

    def insert_adress(self, city, state):
        self.adresses.append(Adress(city, state))

    def list_adresses(self):
        for adress in self.adresses:
            print(f'{adress.city} - {adress.state}')

    def __del__(self):  # Garbage collector
        print(f'{self.name} FOI APAGADO')


class Adress:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):  # Garbage collector
        print(f'{self.city}/{self.state} FOI APAGADO')
