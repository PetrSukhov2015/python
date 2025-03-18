import psycopg2

# Подключение к БД и выполнение запроса
with psycopg2.connect(host="gamma.hi-tech.org", database="ivcs", user="ivcs", password="ivcs") as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM videoconference."domain";')
            #print(cursor.fetchall())
            for row in cursor.fetchall():
                print(row)
