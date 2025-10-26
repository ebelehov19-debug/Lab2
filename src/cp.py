import os.path
from src.pathcorr import*
from src.loggining import*
import shutil
def cpi(ist:str, kuda:str,fl='')->None:
    otk=to_correct(ist)
    fom=to_correct(kuda)
    if not(os.path.exists(otk)):
            erro=f'Данного пути не существует!!'
            print(f"ERROR:{erro}")
            logcom('cp',0,erro)
            return
    if not(os.path.exists(fom)):
            erro=f'Данного пути не существует'
            print(f"ERROR:{erro}")
            logcom('cp',0,erro)
            return
    if os.path.isdir(otk) and fl!='-r':
            erro=f'Не удалось скопировать!!!'
            print(f"ERROR:{erro}")
            logcom('cp',0,erro)
            return
    if os.path.isdir(otk):
           fom = os.path.join(fom, os.path.basename(otk))
           shutil.copytree(otk,fom)
    elif os.path.isfile(otk):
           shutil.copy2(otk,fom)
           print("pop")
    print(f'cp {otk} {fom}')
    logcom(f'cp {otk} {fom}',1,'')
s=input()
a=s.split()
if len(a)==3:
    cpi(a[0],a[1],a[2])

