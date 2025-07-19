import sqlite3
import pandas as pd

with sqlite3.connect('my_data.db') as conn:
    cursor = conn.cursor()
    users = pd.read_csv('users.csv')
    users.to_sql('users', conn, if_exists='append', index=False, chunksize=10000)
    # Выполнение операций с базой данных.
    cursor.execute('SELECT * FROM table_name')
    result = cursor.fetchall()
    print(result)
