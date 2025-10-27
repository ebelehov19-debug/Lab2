from src.pathcorr import*
import os
from src.loggining import*
import shutil
def rm(ist,fl):
    
    if ist in ['/', '..', '.'] or ist == os.path.dirname(ist):
            error = "Невщзмажно удалить директорию"
            print(f"Error: {error}")
            logcom(f"rm", 0, error)
            return
    otk=to_correct(ist)
    if not(os.path.exists(otk)):
        erro=f'Данного пути не существует!!'
        print(f"ERROR:{erro}")
        logcom('rv',0,erro)
        return
    if os.path.isdir(otk) and fl!='-r':
        erro=f'Не удалось удалить!!!'
        print(f"ERROR:{erro}")
        logcom('rm',0,erro)
        return
    t=input("Действительно хотите удалить? (y/n)")
    if t.lower()!='y':
        print("Удаление отменено")
        logcom("rm",0,'Удаление отменено')
    else:
        if os.path.isdir(otk):
            shutil.rmtree(otk)
        if os.path.isfile(otk):
            os.remove(otk)
        logcom('rm',1,'')    
s=input().split()
if len(s)==2:
    rm(s[0],s[-1])    
    
