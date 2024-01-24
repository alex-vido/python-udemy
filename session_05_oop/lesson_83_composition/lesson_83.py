from classes import Client

client_1 = Client('Alex', 29)
print(client_1.name, end=': ')
client_1.insert_adress('São Paulo', 'SP')
client_1.list_adresses()
del client_1
print()

client_2 = Client('João', 68)
print(client_2.name, end=': ')
client_2.insert_adress('Belo Horizonte', 'MG')
client_2.list_adresses()
del client_2
print()

client_3 = Client('Rudnei', 47)
print(client_3.name, end=': ')
client_3.insert_adress('Acre', 'AM')
client_3.list_adresses()
del client_3
print()

print('\n', '#' * 120, '\n')
