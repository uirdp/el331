import FileManager
import DatabaseManager


def main():

    db = DatabaseManager.DatabaseManager()
    db.open_database()

    command = input("choose operation, u:upload file, s:show file content, d:delete file, a:all files ud:update file ")

    if command == 'u':
        upload_file(db)
    elif command == 's':
        show_file_from_database(db)
    elif command == 'd':
        a = 3
    elif command == 'ud':
        a = 4
    elif command == 'a':
        show_all_files_from_database(db)
    else:
        print('bad command, try again')


def upload_file(db):

    path = input('input path to the file ')
    file_manager = FileManager.FileManager()

    name, content = file_manager.get_file_content(path)

    db.insert_to_database(db.conn, name, content)

def show_file_from_database(db):
    option = input('search by name or id?: n or i: ')
    if option == 'n':
        option = input('use original or updated name?　o or u: ')
        if option == 'o':
            name = input('input the original name of the file: ')
            db.show_data_from_origninal_name(db.conn, name)

def show_all_files_from_database(db):
    db.show_all_data(db.conn)

if __name__ == "__main__":
    main()