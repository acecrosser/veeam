import random


class TestCase():
    
    def __init__(self, tc_id=random.randint(1, 100), name=None):
        self.tc_id = tc_id
        self.name = name

    def prep(self):
        pass

    def run(self):
        pass

    def clean_up(self):
        pass

    def execute(self):
        if self.prep() == True:
            print('Тест-кейс остановлен')
        else:            
            print(self.run())


class OneFile(TestCase):
    
    def prep(self):
        from time import time
        time_now = int(time())
        if time_now % 2 == 0:
            return True

    def run(self):
        import os
        user = os.getlogin()
        if os.name == 'nt':
            home_path = os.path.join('C:\\Users\\' + user.title())
            list_dir = os.listdir(home_path)
            return list_dir
        elif os.name == 'posix':
            home_path = os.path.join('/home/' + user)
            list_dir = os.listdir(home_path)
            return list_dir
        else:
            return ('Вы находитесь в ОС, которая не поддерживается')

    
class ManyFile(TestCase):
    
    def prep(self):
        import psutil
        total_memory = (psutil.virtual_memory().total / 100000)
        if 1024 > int(total_memory):
            return True

    def run(self):
        import os
        with open('test', 'wb') as file:
            file.write(os.urandom(1024000))
        return ('Файл tets успешно создан')

    def clean_up(self):
        import os
        os.remove(os.path.abspath('test'))
        return ('Файл tets успешно удален')

