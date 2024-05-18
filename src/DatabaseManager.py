import sqlite3

class DatabaseManager:

    def __init__(self):
        conn = []
    def open_database(self):
        dbname = '.database'
        self.conn = sqlite3.connect(dbname)
        self.create_database()

    #他パラメータを受け取ってidで返す
    def translate_to_id(self, g, t):
        cur = self.conn.cursor()

        if t == 'id':
            return g

        if t == 'original_name':
            cur.execute('SELECT id FROM items WHERE original_name=?', (g,))
            return cur.fetchone()[0]

        elif t == 'updated_name':
            cur.execute('SELECT id FROM items WHERE updated_name=?', (g,))
            return cur.fetchone()[0]





    def create_database(self):
        cur = self.conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_name TEXT UNIQUE,
        updated_name TEXT UNIQUE,
        content TEXT)""")

        self.conn.commit()

    def insert_to_database(self, filename, content):
        cur = self.conn.cursor()

        cur.execute('INSERT INTO items(original_name, content) VALUES (?,?);', (filename, content))
        self.conn.commit()

    def show_data_from_origninal_name(self, filename):
        cur = self.conn.cursor()

        cur.execute('SELECT * FROM items WHERE original_name=?', (filename,))
        print(cur.fetchall())

    def delete_from_database(self, filename):
        cur = self.conn.cursor()
        cur.execute('DELETE FROM items WHERE original_name=?', (filename,))

        self.conn.commit()


    def show_all_data(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM items')