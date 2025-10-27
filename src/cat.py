from os.path import*
from src.pathcorr import*
from src.loggining import*
def catti(cmd:str)->None:
    try:
        puti=to_correct(cmd)
        if not(exists(puti)):
            erro=f'Данного пути не существует'
            print(f"{erro}")
            logcom(f'cat{puti}',0,erro)
            return
        if isdir(puti):
            erro=f'Является директорией'
            print(f"{erro}")
            logcom(f'cat{puti}',0,erro)
            return
        if isfile(puti):
            with __builtins__.open(puti,'r') as file:
                for line in file:
                    print(line)
        logcom(f'cat {puti}',1,'')
    except Exception as errors:
        print(f"Error {errors}")
        logcom(f'cat',0,errors)

s=input()
catti(s)

