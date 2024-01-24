import pymysql.cursors
from contextlib import contextmanager

# CRUD - CREATE, READ, UPDATE, DELETE

@contextmanager
def connect():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='alex-vido',
        password='14092019',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield connection
    finally:
        connection.close()


# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'

#         data = [
#             ('Muriel', 'Figueiredo', 19, 55,),
#             ('Rose', 'Figueiredo', 55, 68,),
#             ('José', 'Figueiredo', 60, 75,),
#         ]

#         cursor.executemany(sql, data)
#         connection.commit()

# DELETA UM REGISTRO NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         connection.commit()

# DELETA VÁRIOS REGISTROS NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         connection.commit()

# DELETA VÁRIOS REGISTRO NA BASE DE DADOS ENTRE UM ID E OUTRO
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s and %s'
#         cursor.execute(sql, (3, 5))
#         connection.commit()

# # ATUALIZA UM NOME NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('Joana', 2))
#         connection.commit()

# ESTE SELECIONA OS DADOS DA BASE DE DADOS
with connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')  # DESC para ser do último para o 1
        result = cursor.fetchall()

        for line in result:
            print(line)
