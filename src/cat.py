from src.pathcorr import*
from src.loggining import*
import os
def catti(cmd:str)->None:
    """
    функция catti выполняет функцифнал cat - вывод содержимого файла
    сначала происходит нормализация пути 
    Далее идет проверка пути на существование если нет то ошибка
    проверка на директорию если да то ошибка 
    проверка на файл если да то дальше происходит чтение файла и его вывод
    
    """
    try:
        puti=to_correct(cmd)
        if not(os.path.exists(puti)):
            erro=f'Данного пути не существует'
            print(f"{erro}")
            logcom(f'cat {puti}',0,erro)
            return
        if os.path.isdir(puti):
            erro=f'Является директорией'
            print(f"{erro}")
            logcom(f'cat {puti}',0,erro)
            return
        if os.path.isfile(puti):
            with open(puti,'r') as file:
                for line in file:
                    print(line)
        logcom(f'cat {puti}',1,'')
    except Exception as e:
        print(f"Error {e}")
        logcom(f'cat',0,e)




