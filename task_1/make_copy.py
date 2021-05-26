import os
from shutil import copy, copytree
import xml.etree.ElementTree as et


def copy_file(path_from: str, path_to: str):
    if not os.path.exists(path_from):
        print('Файл, который вы хотите скопировать - отсутсвует')
    elif not os.path.exists(path_to):
        os.makedirs(path_to)
        copy(path_from, path_to)
        return print(f'Файл {path_from} скопирован ->> {path_to}')
    else:
        try:
            copy(path_from, path_to)
            return print(f'Файл {path_from} скопирован ->> {path_to}')
        except PermissionError as err:
            return print(f'У сожалению у вас не достаточно прав. {err}')


def parameter_check():

    try:
        tree = et.parse(os.path.abspath('config.xml'))
        root = tree.getroot()
        
        for child in root:
            param = child.attrib
            path_from = os.path.join(param['source_path'], param['file_name'])
            path_to = param['destination_path']
            
            if os.name == 'posix' and param['source_path'].startswith('/'):
                copy_file(path_from, path_to)
            elif os.name == 'nt' and param['source_path'][0].isalpha():
                copy_file(path_from, path_to)
            else:
                continue

    except FileNotFoundError as err:
        print(f'К сожалению файл конфигурации - не найден.\n{err}')
    except et.ParseError as err:
        print('Файл конфигурации не соответсвует требованиям')
    except KeyError as err:
        print('Конфигурация не соответсвует требованиям')


if __name__ == '__main__':
    parameter_check()