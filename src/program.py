import FileManager

def main():
    command = input("choose operation, u:upload file, s:show file content, d:delete file, ud:update file ")


    if command == 'u':
        a = 1
    elif command == 's':
        a = 2
    elif command == 'd':
        a = 3
    elif command == 'ud':
        a = 4
    else:
        print('error')

    def upload_file():
        path = input('input path to the file')
        file_manager = FileManager(path)
        file_manager.upload_file()


