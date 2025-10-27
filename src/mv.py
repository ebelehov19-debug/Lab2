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
                logcom(f'mv {otk} {kuda}',0,erro)
                return
        if os.path.isdir(fom):
            shutil.move(otk,fom)
        else:
            pa=os.path.dirname(otk)
            new=os.path.join(pa,kuda)
            rename(otk,new)
        print(f"mv {otk} {kuda}")
        logcom(f"mv {otk} {kuda}",1,'')
    except Exception as e:
         print(f"Error:{e}")
         logcom(f'rm',0,str(e))
s,s1=input().split()
mv(s,s1)   
