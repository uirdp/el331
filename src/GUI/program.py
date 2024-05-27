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
    elif command == 'dg':
        g = '../sample2.txt'
        db.translate_to_id(g, 'original_name')
    elif command == 'r':
        db.reset_database()
    else:
        print('bad command, try again')


def upload_file(db):

    path = input('input path to the file ')
    file_manager = FileManager.FileManager()

    name, content = file_manager.get_file_content_and_name(path)

    db.insert_to_database(name, content)

def show_file_from_database(db):
    option = input('search by name or id?: n or i: ')
    if option == 'n':
        option = input('use original or updated name?　o or u: ')
        if option == 'o':
            name = input('input the original name of the file: ')
            id = db.translate_to_id(name, 'original_name')
            db.show_data(db.conn, id)


def delete_file_from_database(db):
    target_name_or_id = input('input either name or id of the file: ')
    option = input('search by name or id?: n or i: ')

    if option == 'n':
        option = input('original or updated name? o or u: ')
        if option == 'o':
            id = db.translate_to_id(target_name_or_id, 'original_name')
            db.delete_data(db.conn, id)


def show_all_files_from_database(db):
    db.show_all_data()

if __name__ == "__main__":
    main()