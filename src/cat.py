from os.path import*
from src.pathcorr import*
from src.loggining import*
def catti(cmd:str)->None:
    puti=to_correct(cmd)
    print(puti)
    if not(exists(puti)):
        erro=f'Данного пути не существует'
        print(f"ERROR:{erro}")
        logcom('cat',0,erro)
        return
    if isdir(puti):
        erro=f'Является директорией'
        print(f"ERROR:{erro}")
        logcom('cat',0,erro)
        return
    if isfile(puti):
        with __builtins__.open(puti,'r') as file:
            for line in file:
                print(line)
    logcom(f'cat {puti}',1,'')
s=input()
catti(s)

