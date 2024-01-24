"""

public, protected, private  # Not exist in Python
_ weak private/protected (public_)  # Steal possible to acess it, out of the class
__ strong private (_CLASSNAME__ATTRIBUTENAME) # In that way, if someone try to acess, it create a new attribute,
protecting the attribute in the class

"""

class DataBase:
    def __init__(self):
        self.__data = {}

    # Getter
    @property
    def data(self):
        return self.__data

    def client_insert(self, id, name):
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def clients_list(self):
        for id, name in self.__data['clients'].items():
            print(id, name)

    def client_erase(self, id):
        del self.__data['clients'][id]

db = DataBase()

db.client_insert(1, 'Alex')
db.client_insert(2, 'Kelly')
db.client_insert(3, 'Guilherme')
db.client_insert(4, 'Arthur')
db.client_insert(5, 'Enzo Gabriel')
db.client_insert(6, 'Pedro Rubens')
db.client_insert(7, 'Yuri')
db.client_insert(8, 'Neguinha')

# with getter
print(db.data)


# without getters and setters
"""
db.data = 'Alex'  # In this way, we broke all the methods.
db._data = 'Alex'  # In this way, it's a convention that method is'nt to be acessed out of the class
db.__data = 'Alex'  # In this way, it created a new attribute, protecting the attribute in the class
print(f'{db.__data}\n')
print(db._DataBase__data)  # To acess the real attribute
"""

db.client_erase(8)

db.clients_list()
