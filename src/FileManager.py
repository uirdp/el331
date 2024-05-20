import DatabaseManager
import os
import datetime

class FileManager:

    def get_file_content_and_name(self, path):

        with open(path, 'r') as f:
            s = f.read()
            n = os.path.basename(path).split('.',1)[0]

        return n, s

    def save_search_results(self, text, number, term):
        dt = datetime.datetime.now()
        ds = dt.strftime('%Y-%m-%d-%H%M%S')

        file_name = str(number) + ds + term
        path = 'result-' + file_name + '.txt'

        f = open(path, 'w')
        f.write(text)
        f.close()

        print(path)

