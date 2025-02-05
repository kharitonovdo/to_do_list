import sqlite3


connection = sqlite3.connect('to_do_list.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DANNIE (
    id INTEGER PRIMARY KEY,
    username TEXT
    )
''') 
connection.commit()
connection.close()


def added(text):
    connection = sqlite3.connect('to_do_list.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO DANNIE (username) VALUES(?)', (text, ))
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect('to_do_list.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM DANNIE WHERE id=?', (id,)) 
    connection.commit()
    connection.close()