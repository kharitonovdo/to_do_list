import sqlite3


connection = sqlite3.connect('to_do_list.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DANNIE (
    id INTEGER PRIMARY KEY,
    username TEXT,
    galka INTEGER
    )
''') 
connection.commit()
connection.close()


def added(text):
    connection = sqlite3.connect('to_do_list.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO DANNIE (username, galka) VALUES (?, ?)', (text, 0))
    connection.commit()
    connection.close()

def delete(id):
    connection = sqlite3.connect('to_do_list.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM DANNIE WHERE id=?', (id,)) 
    connection.commit()
    connection.close()

def get_text():
    connection = sqlite3.connect('to_do_list.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM DANNIE')
    text = cursor.fetchall()
    connection.close()
    return text

def galka(id, bolev):
    connection = sqlite3.connect('to_do_list.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE DANNIE SET galka=? WHERE id=?', (bolev, id,))
    connection.commit()
    connection.close()