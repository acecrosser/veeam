### Задача 1
Реализовать программу, осуществляющую копирование файлов в соответствии с конфигурационным файлом. Конфигурационный файл должен иметь формат xml. Для каждого файла в конфигурационном файле должно быть указано его имя, исходный путь и путь, по которому файл требуется скопировать.

**Пример:**

Конфигурационный файл:
```
<config>    
    <file
        source_path="C:\Windows\system32"
        destination_path="C:\Program files"
        file_name="kernel32.dll"    
    />
    <file
        source_path="/var/log"
        destination_path="/etc"
        file_name="server.log"
    />
</config>
```

**Для проверки работы скрипта, следуйте инструкцией ниже:**

Скопируйте репозиторий к себе на локальный ПК:

`git clone https://acecrosser/veeam.git`

Перейдите в папку veeam/task_1:

`cd veeam/task_1`

Внесите в файл `config.xml` желаемые данные для копируемых файлов.

Запустите скрипт от имени администратора:

`python make_copy.py` - Windows

`sudo python3 make_copy.py` - Linux
