from os import*
from datetime import*
from src.loggining import*
from src.pathcorr import*
def ls(cmn=str,fl=str)->None:
    try:
        puti="C::::"
        if cmn: puti= to_correct(cmn)
        else: puti=getcwd()
        if os.path.exists(puti):
            filanddir=listdir(puti)  
            if fl=='-l':
                for i in filanddir:
                    stats = stat(i)
                    size = stats.st_size 
                    raz = oct(stats.st_mode)[-3:] 
                    tim = stats.st_mtime
                    dat=datetime.fromtimestamp(tim).strftime('%Y-%m-%d %H:%M:%S')
                    print(f'{i} {size} {dat} {raz}')
            else:
                for i in filanddir:
                    print(i)
            logcom(f'ls {puti}',True,'')
        else:
            osh= f'Данный путь не существует {puti}'
            print(f'ERROR: {osh}')
            logcom(f'ls {puti}',0,f'ERROR: {osh}')
    except Exception as errors:
        print(f"Error {errors}")
        logcom(f'ls {errors}',0,errors)







