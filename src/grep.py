import os
import re
from src.loggining import*
def grep(pattern:str,path:str,fl='',fl2=''):
    try:
        if fl2=='-i':
            flag = re.IGNORECASE 
        else: flag=0
        pater = re.compile(pattern,flag)
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
                        if pater.search(line):
                            cnt+=1
                            print(f'{pat.replace('')} {i} {line}')
        elif cnt==0:
            print("Нет совпадений")
    except Exception as err:
        print(f"ERROR:{str(err)}")


    
    



    