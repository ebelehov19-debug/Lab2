from src.pathcorr import*
from src.loggining import*
def catti(cmd)->None:
    print(cmd)
    if True:
        puti=to_correct(cmd)
        if not(os.path.exists(puti)):
            erro=f'Данного пути не существует'
            print(f"{erro}")
            logcom(f'cat{puti}',0,erro)
            return
        if os.path.isdir(puti):
            erro=f'Является директорией'
            print(f"{erro}")
            logcom(f'cat{puti}',0,erro)
            return
        print(puti)
        if os.path.isfile(puti):
            with open(puti,'r') as file:
                for line in file:
                    print(line)
        logcom(f'cat {puti}',1,'')
    # except Exception as e:
    #     print(f"Error {e}")
    #     logcom(f'cat',0,e)




