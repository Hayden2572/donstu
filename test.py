import psycopg2

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
    except OperationalError as e:
        print('bad connection to db')
    return connection
connection = create_connection("database", "postgres", "admin", "localhost", "5432")

cursor = connection.cursor()
cursor.execute("INSERT INTO database.usr_info (id, user_id) VALUES (0, 6623770793)")
connection.commit()
print("1 запись успешно вставлена")
cursor.execute("SELECT * FROM database.usr_info")
record = cursor.fetchall()
print(f"Результат {record}")