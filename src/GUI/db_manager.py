import sqlite3

class db_manager:

    def init(self):
        dbname = '.db'
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()


    def create_database():
        # texts
        cur.execute('CREATE TABLE
        text(
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_name TEXT UNIQUE,
        updated_name,
        content String
        )')

    def insert_into_database(TextType, name, content):
        if TextType == 'Q':
            cur_Q.execute('INSERT INTO Q_text(
            name TEXT UNIQUE,
            content String
            )')
        elif TextType == 'K':
            cur_K.execute('INSERT INTO K_text(
            name TEXT UNIQUE,
            content String
            )')
        elif TextType == 'R':
            cur_R.execute('INSERT INTO R_text(
            name TEXT UNIQUE,
            content String
            )')
        else:
            print('not valid')
