import os
import re
from src.loggining import*
def grep(pattern:str,path:str,fl='',fl2=''):
    if fl2=='-i':
        flag = re.IGNORECASE 
    else: flag=0
    pat = re.compile(pattern,flag)
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
            logcom(f"grep {path}",0,"Используйте -r для поиска в директории")
    fis=[i for i in file_serch if os.path.isfile(i)]
    cnt=0
    if len(fis)==0:
        print("Нет файлов для поиска")
        logcom("grep",0,"Нет файлов для поиска")
    else:
        for pat in fis:
            with open(pat,'r') as file:
                i=0
                for line in files:
                    i+=1
                    if pattern.search(line):
                        cnt+=1
                        print(f'{pat} {i} {line}')
    if cnt==0:
        print("Нет совпадений")

    
    



    