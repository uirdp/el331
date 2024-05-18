import DatabaseManager

class FileManager:

    def get_file_content(self, path):

        with open(path, 'r') as f:
            s = f.read()
            n = f.name
        return n, s



