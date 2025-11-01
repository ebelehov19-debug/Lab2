from src.pathcorr import*
import os
from src.loggining import*
import shutil
def rm(ist:str,fl='')->None:
    """
    rm - удаление файлов или директорий
    сначала происходит проверка на удаление важных диреторий и выдается ошибка при надобности 
    далее нормализация пути 
    проверка существования пути если нет то ошибка
    проверка если диретория и не тот флаг выдается ошибка
    далее происходит действительно ли пользователь хочет удалить 
    далее иде т проверка на директории и файлы и происходит удаление 

    """
    try:
        if ist in ['/', '..', '.'] or ist == os.path.dirname(ist):
            error = "Невозмажно удалить директорию"
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
            logcom(f'rm{fl}{otk}',0,erro)
            return
        t=input("Действительно хотите удалить? (y/n)\n")
        if t.lower()!='y':
            print("Удаление отменено")
            logcom(f"rm{fl}{otk}",0,'Удаление отменено')
        else:
            if os.path.isdir(otk):
                shutil.rmtree(otk)
            if os.path.isfile(otk):
                os.remove(otk)
            logcom(f'rm{fl}{otk}',1,'')    
    except Exception as e:
        print(str(e))
        logcom(f'rm',0,str(e))


