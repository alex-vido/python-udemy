import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS clients ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'name TEXT,'
               'weight REAL'
               ')')

# cursor.execute('INSERT INTO clients (name, weight) VALUES ("Alex Vido", 80.5)')
# connection.commit()

# cursor.execute('INSERT INTO clients (name, weight) VALUES (?, ?)', ('Kelly', 67))
# cursor.execute(
#     'INSERT INTO clients (name, weight) VALUES (:name, :weight)',
#     {'name': 'Yuri', 'weight': 9}
# )
# cursor.execute(
#     'INSERT INTO clients VALUES (:id, :name, :weight)',
#     {'id': None, 'name': 'Pedro Rubens', 'weight': 13}
# )
# connection.commit()

# cursor.execute(
#     'UPDATE clients SET name=:name WHERE id=:id',
#     {'name': 'Enzo', 'id': 2}
# )
# connection.commit()

# cursor.execute(
#     'DELETE from clients WHERE id=:id',
#     {'id': 8}
# )
# connection.commit()

# cursor.execute('SELECT * FROM clients')

# for line in cursor.fetchall():
#     ident, name, weigth = line

#     print(ident, name, weigth)

cursor.execute(
    'SELECT name, weight FROM clients WHERE weight > :weight',
    {'weight': 50}
)

for line in cursor.fetchall():
    name, weight = line

    print(name, weight)


cursor.close()
connection.close()
