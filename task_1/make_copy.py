import os
from shutil import copy
import xml.etree.ElementTree as et


tree = et.parse(os.path.abspath('config.xml'))
root = tree.getroot()

for child in root:
    tag = child.tag, 
    param = child.attrib
    if os.name == 'posix' or param['source_path'].startswith('/'):
        print('Ты делаешь копию для линукса')
    else:
        print('Ты в винде')
        # TODO Сделать проверку наличия файла
        # TODO Вынести в отдельную функцию сам способ копирования  
        try:
            full_path = os.path.join(param['source_path'], param['file_name'])
            path_to_copy = os.path.join(param['destination_path'])
            copy(full_path, path_to_copy)
            print('Файл успешно скопирован')
        except PermissionError as err:
            print(err, "Скрипт запущен без прав")