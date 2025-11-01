import os
import re
from src.loggining import*
from src.pathcorr import*
def grep(pattern:str,path:str,fl='',fl2=''):
    """
    grep- поиск в файлах по переданному шаблону 
    идет выполнение регулярного выражение и переменение нужных флагов
    проверка на файл и его добавление
    если директория то проходи по всем поддиректориям и собирание файлов в лист еще проверка на нужный флаг
    далее удаляем все диретории 
    потом идем по файлам и смотрем совпадение с регулярным выражением и выводим файл номер строки и ее содиржимое 
    если ничего не нашлось выводится сообщение 
    """
    try:
        path=to_correct(path)
        if not(os.path.exists(path)):
            erro=f'Данного пути не существует'
            print(f"{erro}")
            return
        pater = re.compile(pattern)
        file_serch=[]
        if os.path.isfile(path):
            if fl:
                print("Используйте -r для поиска в директории")
                return
            file_serch.append(path)
        if os.path.isdir(path):
            if fl=='-r':
                for root, dirs, files in os.walk(path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        file_serch.append(full_path)
            else:
                print("Используйте -r для поиска в директории")
                return
        fis=[i for i in file_serch if os.path.isfile(i)]
        cnt=0
        if len(fis)==0:
            print("Нет файлов для поиска")
        elif len(fis)!=0:
            for pat in fis:
                with open(pat,'r') as filp:
                    i=0
                    for line in filp:
                        i+=1
                        lin=line
                        if(fl2=='-i'):
                            lin=line.lower()
                        if pater.search(lin):
                            cnt+=1 
                            print(f'{pat} {i} {line}')
        if cnt==0:
            print("Нет совпадений")
    except Exception as err:
        print(f"ERROR:{str(err)}")


    
    



    