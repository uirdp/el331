import sqlite3

class DatabaseManager:

    def __init__(self):
        conn = []
    def open_database(self):
        dbname = '.database'
        self.conn = sqlite3.connect(dbname)
        self.create_database()

    def create_database(self):
        cur = self.conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_name TEXT UNIQUE,
            updated_name TEXT UNIQUE,
            content TEXT)""")

        self.conn.commit()

    #他パラメータを受け取ってidで返す
    def translate_to_id(self, user_input, input_type):
        cur = self.conn.cursor()

        if input_type == 'id':
            return user_input

        if input_type == 'original_name':
            cur.execute('SELECT id FROM items WHERE original_name=?', (user_input,))
            return cur.fetchone()[0]

        elif input_type == 'updated_name':
            cur.execute('SELECT id FROM items WHERE updated_name=?', (user_input,))
            return cur.fetchone()[0]




    def reset_database(self):
        cur = self.conn.cursor()
        cur.execute('DROP TABLE IF EXISTS items')


    def insert_to_database(self, filename, content):
        cur = self.conn.cursor()

        cur.execute('INSERT INTO items(original_name, content) VALUES (?,?);', (filename, content))
        self.conn.commit()

        self.show_data(cur.lastrowid)
        print('data inserted ')

    def get_content(self, id):
        cur = self.conn.cursor()

        cur.execute('SELECT content FROM items WHERE id=?', (id,))
        s = cur.fetchone()[0]

        return s

    def delete_from_database(self, id):
        cur = self.conn.cursor()

        cur.execute('DELETE FROM items WHERE id=?', (id,))

        self.conn.commit()


    def show_all_data(self):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM items')