import sqlite3
from enum import Enum

class TextType(Enum):
    Q = 1
    K = 2
    R = 3

class FileManager:

    def __init__(self, path):
        self.path = path

    def get_text_type(self):
        text_type = int(input('Q = 1, K = 2, R = 3'))
        if type == TextType.Q:
            return 'Q'
        elif type == TextType.K:
            return 'K'
        elif type == TextType.R:
            return 'R'
        else:
            # 不正な入力のばあいやり直す
            print('not valid')
            self.get_text_type()

    # Create files
    def upload_file(self):

        with open(self.path, 'r') as file:
            s = file.read()
            text_type = self.get_text_type()
            name = text_type + '1.txt'
            # id = db_manager.get_biggest_id(text_type) -> text_type + id + '.txt'
            # db_manager.insert_to_database(s, name)

    # Retrieve files
    def get_file_content_from_id(self, text_type, id):

            s = 'placeholder'
            # s = db_manager.get_text_content(text_type, id)
            print(s)

    def get_file_content_from_name(self, text_type, name):
        s = 'placeholder'
        # s = db_manager.get_text_content_from_name(name)
        print(s)



