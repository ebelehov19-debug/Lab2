from src.pathcorr import*
from src.loggining import*
import shutil
import os
def cpi(ist:str, kuda:str,fl='')->None:
    """
    функция cpi выполняет функционал cp - копирование файлов/директорий  
    просхоидт нормализация переданных аргументов 
    Далее идет провера на существование обоих путей  если нет то ошибка
    далее идут проверки флага и проверка на директори при корректном вводе происходит копирование директории с помощью shutil.copytree(otk,fom)
    если является файлом происходит копирование файла shutil.copy2(otk,fom)
    """
    try:
        otk=to_correct(ist)
        fom=to_correct(kuda)
        if not(os.path.exists(otk)):
                erro=f'Данного пути не существует!!'
                print(f"{erro}")
                logcom(f'cp {otk} {fom}',0,erro)
                return
        if not(os.path.exists(fom)):
                erro=f'Данного пути не существует'
                print(f"ERROR:{erro}")
                logcom(f'cp{otk} {fom}',0,erro)
                return
        if os.path.isdir(otk):
                if fl!='-r':
                        erro=f'Не удалось скопировать!!!'
                        print(f"{erro}")
                        logcom(f'cp {fl} {otk} {fom}',0,erro)
                        return
                elif fl =='-r':
                        fom = os.path.join(fom, os.path.basename(otk))
                        shutil.copytree(otk,fom)
        elif os.path.isfile(otk):
                shutil.copy2(otk,fom)
        logcom(f'cp {fl} {otk} {fom}',1,'')
    except Exception as e:
        print(str(e))
        logcom(f'cp',0,str(e))


