# This lesson is for explain with you wouldn't use mutable params in functions

# ex mutables: lists, dicts
# ex immutables: strings, numbers, bool, None

"""
# In this way, all the lists will have the same values
def clients_list(clients_iterable, lst=[]):
    lst.extend(clients_iterable)
    return lst

client_list_1 = ['Atila']
clients_1 = clients_list(['Alex', 'Kelly', 'Lucimara'], client_list_1)
clients_2 = clients_list(['Gui', 'Thu', 'Biel', 'Rubinho', 'Yuh'])
clients_3 = clients_list(['João'])
print(clients_1)
print(clients_2)
print(clients_3)
"""

# This way resolves the problem
def clients_list(clients_iterable, lst=None):
    if lst is None:
        lst = []
    lst.extend(clients_iterable)
    return lst

client_list_1 = ['Atila']
clients_1 = clients_list(['Alex', 'Kelly', 'Lucimara'], client_list_1)
clients_2 = clients_list(['Gui', 'Thu', 'Biel', 'Rubinho', 'Yuh'])
clients_3 = clients_list(['João'])
print(clients_1)
print(clients_2)
print(clients_3)
