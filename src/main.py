from os import*
from shutil import*
from datetime import*
from logging import*
from src.ls import*
from src.cd import*
from src.cat import*
def main() -> None: 
       s=input()
       a=s.split()
       print(a)
       if len(a):
            # if a[0].lower()=='ls'and len(a)==2:
            #     ls(a[1],'')
            # elif len(a)==3:
            #     ls(a[1],a[2])
            #     print('tt')
            # else:
            #     print("ERROR: ls")
            #     logcom(f'ls {s}',0,'некорректный ввод')
            # if a[0].lower()=='cd' and len(a)==2:
            #      cd(a[1])
            # else:
            #     print("ERROR: cd")
            #     logcom(f'cd {s}',0,'некорректный ввод')
            if a[0]=='cat':
                  catti(a[1])
            else:
                 print("ERROR: cd")
                 logcom(f'cd {s}',0,'некорректный ввод')
                 
                 
main()   
                   
       
