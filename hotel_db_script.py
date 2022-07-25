import psycopg2

conn = psycopg2.connect('dbname=hoteldb user=ali')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS hotel CASCADE;')
cursor.execute('DROP TABLE IF EXISTS room;')

cursor.execute('''
               CREATE TABLE hotel (
                   hotel_id SERIAL PRIMARY KEY,
                   name VARCHAR (50) NOT NULL,
                   country VARCHAR (25) NOT NULL
               );
               ''')
cursor.execute('''
               CREATE TABLE room (
                   room_no INTEGER PRIMARY KEY,
                   hotel_id SERIAL REFERENCES hotel(hotel_id),
                   type VARCHAR(15) NOT NULL,
                   price INTEGER NOT NULL
               );
               ''')

SQL_QUERY_1 = 'INSERT INTO hotel (hotel_id, name, country) VALUES (%(hotel_id)s, %(name)s, %(country)s);'
data_dict_1 = (
            {'hotel_id': 1, 'name': 'Eko Hotel', 'country': 'Nigeria'},
            {'hotel_id': 2, 'name': 'Hilltop Hotel', 'country': 'Tunisia'},
            {'hotel_id': 3, 'name': 'Golden Tulip Hotel', 'country': 'Kenya'},
            {'hotel_id': 4, 'name': 'Clairmont Hotel', 'country': 'Egypt'},
            {'hotel_id': 5, 'name': 'Devon Hotel', 'country': 'Nigeria'},
            {'hotel_id': 6, 'name': 'City Base Hotel', 'country': 'Cameroun'}
)
            
cursor.executemany(SQL_QUERY_1, data_dict_1)

SQL_QUERY_2 = '''INSERT INTO room (room_no, hotel_id, type, price) VALUES
                (%(room_no)s, %(hotel_id)s, %(type)s, %(price)s);
              '''
data_dict_2 = (
    {'room_no': 101, 'hotel_id': 1, 'type': 'Smoking', 'price': 150},
    {'room_no': 412, 'hotel_id': 5, 'type': 'Non-Smoking', 'price': 200},
    {'room_no': 126, 'hotel_id': 4, 'type': 'Non-Smoking', 'price': 200},
    {'room_no': 128, 'hotel_id': 6, 'type': 'Smoking', 'price': 800},
    {'room_no': 876, 'hotel_id': 2, 'type': 'Non-Smoking', 'price': 500},
    {'room_no': 898, 'hotel_id': 1, 'type': 'Smoking', 'price': 200},
    {'room_no': 345, 'hotel_id': 3, 'type': 'Non-Smoking', 'price': 1000},
    {'room_no': 467, 'hotel_id': 4, 'type': 'Non-Smoking', 'price': 500},
    {'room_no': 100, 'hotel_id': 5, 'type': 'Non-Smoking', 'price': 150},
    {'room_no': 120, 'hotel_id': 4, 'type': 'Non-Smoking', 'price': 700},
    {'room_no': 257, 'hotel_id': 3, 'type': 'Non-Smoking', 'price': 500},
    {'room_no': 221, 'hotel_id': 2, 'type': 'Non-Smoking', 'price': 150}
)

cursor.executemany(SQL_QUERY_2, data_dict_2)

conn.commit()

cursor.close()
conn.close()
