from src.pathcorr import*
from os import*
from src.loggining import*
import shutil
def mv(ist,kuda):
    otk=to_correct(ist)
    fom=to_correct(kuda)
    if not(os.path.exists(otk)):
            erro=f'Данного пути не существует!!'
            print(f"ERROR:{erro}")
            logcom('mv',0,erro)
            return
    #изучить pathlib для проверки безопасности 
    if os.path.isdir(otk):
         shutil.move(otk,fom)
    if os.path.isfile(otk):
          shutil.move(otk,kuda)
    print(f"mv {otk} {kuda}")
    logcom("mv",1,'')
s,s1=input().split()
mv(s,s1)   
