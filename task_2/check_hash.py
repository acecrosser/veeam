import sys
import os
import hashlib
           

def check_hash(file_name: str, method: str, file_in_folder: str, hash_from_file: str):
    def read_file_for_hash(command):
        with command:
            return command.read()
    try:
        hash_file = getattr(hashlib, method)(read_file_for_hash(open(file_in_folder, 'rb'))).hexdigest()
        if hash_file == hash_from_file:
            print(f'{file_name} - [OK]')
        else:
            print(f'{file_name} - [FAIL]')
    except FileNotFoundError as err:
        print(f'{file_name} - [NOT FOUND]')
    except AttributeError as err:
        print(f'{file_name} - [HASH METHOD NOT FOUND]')


def read_checkfile(file_path: str, folder_path: str) -> str:
    files_in_folder = os.path.join(folder_path)
    file_for_read = os.path.join(file_path)
    with open(file_for_read, 'r') as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            file_in_folder = os.path.join(files_in_folder, line[0])
            try: 
                file_name, method, hash_from_file = (line[0], line[1], line[2])
                check_hash(file_name, method, file_in_folder, hash_from_file)
            except IndexError as err:
                print(f'{file_name} - [NO DATA]')


if __name__ == '__main__':

    input_items = sys.argv
    input_file = input_items[1]
    path = input_items[2]

    if not os.path.exists(input_file):
        print(f'{input_file} - данный файл не найдет, либо вы указали не полный путь к файлу.')
    elif not os.path.exists(path):
        print(f'{path} - данная папка не найдена, либо вы указали не полный путь')
    else:
        read_checkfile(input_file, path)
