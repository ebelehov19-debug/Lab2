import os
import re
from src.loggining import*
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
        pater = re.compile(pattern)
        file_serch=[]
        if os.path.isfile(path):
            file_serch.append(path)
        elif os.path.isdir(path):
            if fl=='-r':
                for root, dirs, files in os.walk(path):
                    for file in files:
                        full_path = os.path.join(root, file)
                        file_serch.append(full_path)
            else:
                print("Используйте -r для поиска в директории")
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
                        if(fl2=='-i'):
                            line=line.lower()
                        if pater.search(line):
                            cnt+=1
                            print(f'{pat} {i} {line}')
        elif cnt==0:
            print("Нет совпадений")
    except Exception as err:
        print(f"ERROR:{str(err)}")


    
    



    