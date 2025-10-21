from os import*
from datetime import*
def ls(cmn):
    filanddir=listdir(getcwd())  
    if cmn[-2:]=='-l':
        for i in filanddir:
            stats = stat(i)
            size = stats.st_size 
            raz = oct(stats.st_mode)[-3:] 
            tim = stats.st_mtime
            dat=datetime.fromtimestamp(tim).strftime('%Y-%m-%d %H:%M:%S')
            print(tim)
            print(f'{i} {size} {dat} {raz}')
    else:
        for i in filanddir:
            print(i)





