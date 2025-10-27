from src.pathcorr import*
from os import*
from src.loggining import*
import shutil
def mv(ist,kuda):
    try:
        otk=to_correct(ist)
        fom=to_correct(kuda)
        if not(os.path.exists(otk)):
                erro=f'Данного пути не существует!!'
                print(f"ERROR:{erro}")
                logcom('mv',0,erro)
                return
        #изучить pathlib для проверки безопасности 
        if os.path.isdir(fom):
            shutil.move(otk,fom)
        else:
            rename(otk,kuda)
        print(f"mv {otk} {kuda}")
        logcom("mv",1,'')
    except Exception as e:
         print(f"eror {e}")
         logcom(f'rm',0,str(e))
s,s1=input().split()
mv(s,s1)   
