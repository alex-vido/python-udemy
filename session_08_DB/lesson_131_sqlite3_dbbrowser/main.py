import sqlite3

class PhonebookDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def insert(self, name, telephone):
        consult = 'INSERT OR IGNORE INTO phonebook (name, telephone) VALUES (?, ?)'
        self.cursor.execute(consult, (name, telephone))
        self.conn.commit()

    def edit(self, name, telephone, id):
        consult = 'UPDATE OR IGNORE phonebook SET name=?, telephone=? WHERE id=?'
        self.cursor.execute(consult, (name, telephone, id))
        self.conn.commit()

    def delete(self, id):
        consult = 'DELETE FROM phonebook WHERE id=?'
        self.cursor.execute(consult, (id,))
        self.conn.commit()

    def list(self):
        self.cursor.execute('SELECT * FROM phonebook')

        for line in self.cursor.fetchall():
            print(line)

    def search(self, value):
        consult = 'SELECT * FROM phonebook WHERE name LIKE ?'
        self.cursor.execute(consult, (f'%{value}%',))

        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    phonebook = PhonebookDB('phonebook.db')
    # phonebook.insert('Alex', '111111')
    # phonebook.insert('Kelly', '111112')
    # phonebook.insert('Guilherme', '111113')
    # phonebook.insert('Arthur', '111114')
    # phonebook.insert('Enzo', '111115')
    # phonebook.insert('Pedro', '111116')
    # phonebook.insert('Yuri', '111117')
    # phonebook.edit('Kelly', '222222', '4')
    # phonebook.insert('João', '111118')
    # phonebook.delete(18)
    phonebook.insert('Alexe', '111119')
    phonebook.insert('Aldair Alex João', '111120')
    phonebook.insert('Alex Silva', '111121')
    phonebook.insert('Francisco Alex Forjini', '111122')
    phonebook.insert('Ronaldo Alex A', '111123')
    phonebook.search('Alex')
    # phonebook.list()
