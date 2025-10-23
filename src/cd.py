from os import*
from os.path import*
from src.loggining import*
from src.pathcorr import*
def cd(cmd=str)->None:
    try:
        puti='C::'
        if cmd=='..':
            puti=dirname(getcwd()) 
        else:
            puti=to_correct(cmd)
        print(puti)
        if not(exists(puti)):
            erro=f'Данного пути не существует'
            print(f"ERROR:{erro}")
            logcom('cd',0,erro)
            return
            
        if not(isdir(puti)):
            erro=f'Не Является директорией'
            print(f"ERROR:{erro}")
            logcom('cd',0,erro)
            return
        chdir(puti)
        logcom(f'cd {puti}',1,'')
    except Exception as errors:
        print(f"Error {errors}")
        logcom(f'cd {errors}',0,errors)

        

