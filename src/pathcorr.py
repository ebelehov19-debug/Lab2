import os.path
from os import*
def to_correct(cmn=str)->str:
    if(cmn[0]=='~') :
        cmn=os.path.expanduser(cmn)
    elif (cmn[0]=='.'):
        cmn=os.path.join(getcwd(),cmn)
    return os.path.normpath(cmn)
print(os.path.normpath('c/Users...'))
