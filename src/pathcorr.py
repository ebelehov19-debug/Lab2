import os.path
from os import*
def to_correct(cmn:str)->str:
    puti=cmn
    if (cmn[0])=='~':
        puti=os.path.expanduser(cmn)
    if (cmn[0]=='.'):
        puti=os.path.join(getcwd(),cmn)
    return os.path.normpath(puti).replace("\\","//")
