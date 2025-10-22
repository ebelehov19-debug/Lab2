import os.path
from os import*
def to_correct(cmn=str)->str:
    if (cmn[0]=='.'):
        cmn=os.path.join(getcwd(),cmn)
    return os.path.normpath(cmn)

