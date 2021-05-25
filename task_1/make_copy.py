import os
from shutil import copy
import xml.etree.ElementTree as et


tree = et.parse(os.path.abspath('config.xml'))
root = tree.getroot()


# TODO Проверка корректности адреса, наличие файла
def copy_file(path_from: str, path_to: str):
    try:
        copy(path_from, path_to)
        return print(f'Файл {path_from} скопирован ->> {path_to}')
    except PermissionError as err:
        return print(f'У сожалению у вас не достаточно прав - {err}')


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