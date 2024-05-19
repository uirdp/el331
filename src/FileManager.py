import DatabaseManager
import os

class FileManager:

    def get_file_content_and_name(self, path):

        with open(path, 'r') as f:
            s = f.read()
            n = os.path.basename(path).split('.',1)[0]

        return n, s



