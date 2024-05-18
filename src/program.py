import FileManager
import DatabaseManager


def main():

    db = DatabaseManager.DatabaseManager()
    db.open_database()

    command = input("choose operation, u:upload file, s:show file content, d:delete file, ud:update file ")

    if command == 'u':
        upload_file(db)
    elif command == 's':
        a = 2
    elif command == 'd':
        a = 3
    elif command == 'ud':
        a = 4
    else:
        print('error')


def upload_file(db):

    path = input('input path to the file')
    file_manager = FileManager.FileManager()

    name, content = file_manager.get_file_content(path)

    db.insert_to_database(db.conn, name, content)


if __name__ == "__main__":
    main()