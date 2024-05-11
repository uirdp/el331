import sqlite3
from enum import Enum

class TextType(Enum):
    Q = 1
    K = 2
    R = 3

class FileManager:

    def __init__(self, path):
        self.path = path
        self.type = type

    def get_text_type(self):
        type = int(input('Q = 1, K = 2, R = 3'))
        if type == TextType.Q:
            return 'Q'
        elif type == TextType.K:
            return 'K'
        elif type == TextType.R:
            return 'R'
        else:
            #不正な入力のばあいやり直す
            print('not valid')
            self.get_text_type()
        


    def upload_file(self):
        type = self.get_text_type()

        with open(self.path, 'r') as file:
            s = file.read()
            name = type + id + '.txt'
            #db_manager.insert_to_database(s, name)

    def update_file(self):
        #s = db.get(name)
        #s2 = db.get(name)




