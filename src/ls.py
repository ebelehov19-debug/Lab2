import os
import os.path
from datetime import*
from src.loggining import*
from src.pathcorr import*
def ls(cmn:str,fl:str)->None:
    """
    функция ls - отображение содержимого директории
    на вход подается, которая сначала нормализуется с помощью блока to_correct() и обрабатываем пустой ввод(выводим текущую дирректорию)
    смотрим существует ли этот путь 
    далее смотрим наличие флага, чтобы определиться с выводом файлов 
    если файл есть подробно выводим файлы(с метаданными)
    если флага делаем обычный вывод файлов и директорий
    """
    try:
        puti="C::::"
        t=1
        if cmn: puti= to_correct(cmn)
        else: puti=os.getcwd()
        if os.path.exists(puti):
            filanddir=os.listdir(puti)  
            if fl=='-l':
                for i in filanddir:
                    stats = os.stat(i)
                    size = stats.st_size 
                    raz = oct(stats.st_mode)[-3:] 
                    tim = stats.st_mtime
                    dat=datetime.fromtimestamp(tim).strftime('%Y-%m-%d %H:%M:%S')
                    print(f'{i} {size} {dat} {raz}')
            elif fl=="":
                for i in filanddir:
                    print(i)
            else:
                print("Неправильный флаг")
                logcom(f'ls {puti}',0,f'Неправильный флаг')
                t=0
            if(t):
                logcom(f'ls {fl} {puti}',1,'')
        else:
            osh= f'Данный путь не существует {puti}'
            print(f'ERROR: {osh}')
            logcom(f'ls {puti}',0,f'{osh}')
    except Exception as errors:
        print(f"{errors}")
        logcom(f'ls',0,errors)







