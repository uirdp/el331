import sqlite3

class DatabaseManager:


    def __init__(self):
        conn = []
    def open_database(self):
        dbname = '.database'
        self.conn = sqlite3.connect(dbname)
        self.create_database(self.conn)

    def create_database(self, conn):
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_name TEXT UNIQUE,
        updated_name TEXT UNIQUE,
        content TEXT)""")

        conn.commit()

    def insert_to_database(self, conn, filename, content):
        cur = conn.cursor()

        cur.execute('INSERT INTO items(original_name, content) VALUES (?,?);', (filename, content))
        conn.commit()