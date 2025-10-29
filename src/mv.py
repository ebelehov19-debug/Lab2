from src.pathcorr import*
import os
from src.loggining import*
import shutil
def mvi(ist,kuda):
    if 1:
        otk=to_correct(ist)
        fom=to_correct(kuda)
        print(otk,fom)
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
            os.rename(otk,new)
        print(f"mv {otk} {kuda}")
        logcom(f"mv {otk} {kuda}",1,'')
