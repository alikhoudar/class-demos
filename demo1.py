import psycopg2

connection = psycopg2.connect('dbname=example user=ali')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
               CREATE TABLE table2 (
                   id INTEGER PRIMARY KEY,
                   completed BOOLEAN NOT NULL DEFAULT False
               );
               ''')
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);',(1, True))

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', {
    'id': 2,
    'completed': False
})

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
    'id': 3,
    'completed': False
}

cursor.execute(SQL, data)

cursor.execute('SELECT * FROM table2;')

result = cursor.fetchmany(2)
print('fetchmany', result)

result2 = cursor.fetchone()
print('fetchone', result2)

result3 = cursor.fetchone()
print('fetchone', result3)

connection.commit()

connection.close()
cursor.close()
