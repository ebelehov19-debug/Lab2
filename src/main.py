from os import*
from shutil import*
from datetime import*
from logging import*
from src.ls import*
from src.cd import*
from src.cat import*
from src.cp import*
from src.rm import*
def main() -> None: 
      s=input()
      a=s.split()
      if len(a):
        match a[0]:
            case 'ls':
                  try:
                      if len(a)==2:
                          ls(a[1],'')
                      elif len(a)==3:
                          ls(a[1],a[2])
                      else:
                              print(f"ls некорректный ввод")
                              logcom(f"ls",0,"ls некорректный ввод")
                  except Exception as e:
                        print(f"ls {str(e)}")
                        logcom(f"ls",0,str(e))
            case 'cd':
                  try:
                        if len(a)==2:
                              cd(a[1])
                        else:
                              print(f"cd некорректный ввод")
                              logcom(f"cd",0,"cd некорректный ввод")
                  except Exception as e:
                        print(f"cd {str(e)}")
                        logcom(f"cd",0,str(e))
            case 'cat':
                  try:
                        if len(a)==2:
                                catti(a[1])
                        else:
                              print(f"cat некорректный ввод")
                              logcom(f"cat",0,"cat некорректный ввод")
                  except Exception as e:
                              print(f"cat {str(e)}")
                              logcom(f"cat",0,str(e))
            case 'cp':
                  try:
                        if len(a)==3:
                              cpi(a[1],a[2],'')   
                        if len(a)==4:
                              cpi(a[1],a[2],a[3])
                        else:
                              print(f"cp некорректный ввод")
                              logcom(f"cp",0,"cp некорректный ввод")
                  except Exception as e:
                              print(f"cp {str(e)}")
                              logcom(f"cp",0,str(e))
            case 'rm': 
                  try:
                        if len(a)==2:
                              rm(a[1],'')
                        elif len(a)==3:
                              rm(a[1],a[2])
                        else:
                              print(f"rm некорректный ввод")
                              logcom(f"rm",0,"rm некорректный ввод")
                  except Exception as e:
                              print(f"rm {str(e)}")
                              logcom(f"rm",0,str(e))                               
            case _:print("popa")


                 
main()   
                   
       
