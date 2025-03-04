import sqlite3
import os

db = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(): 
    with open('schema.sql') as f:
        sql = f.read()

    conn = get_db_connection()
    conn.executescript(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    if(os.path.exists(db)):
        response = input('Database Already Exists. Do you want to clean whole data? (y/n): ')
        if response.upper() == 'Y':
            print('Cleaning Database...')
            init_db() 
        else:
            print('Exisiting Database is not cleaned.')    
    else:
        init_db()