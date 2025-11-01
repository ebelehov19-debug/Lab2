from os import*
from os.path import*
from src.loggining import*
from src.pathcorr import*
def cd(cmd:str)->None:
    """
    cd - переход в директории по преданному пути 
    сначала идет обработка специальных случаев путей ..  а другие случаи обрабатывает to_correct()
    далее идет проверка на существование пути если пути нет то ошибка
    и проверка на директорию если не директория то ошибка
    при успешных проверка происходит переход в диреторию с помощью команды chdir()
    """
    try:
        puti='C::'
        if cmd=='..':
            puti=dirname(getcwd()) 
        else:
            puti=to_correct(cmd)
        if not(exists(puti)):
            erro=f'Данного пути не существует'
            print(f"ERROR:{erro}")
            logcom(f'cd {puti}',0,erro)
            return          
        if not(isdir(puti)):
            erro=f'Не Является директорией'
            print(f"ERROR:{erro}")
            logcom(f'cd {puti}',0,erro)
            return
        chdir(puti)
        logcom(f'cd {puti}',1,'')
    except Exception as errors:
        print(f"Error {errors}")
        logcom(f'cd',0,errors)

        

